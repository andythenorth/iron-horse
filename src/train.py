import global_constants # expose all constants for easy passing to templates
import utils

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import codecs

import math
from string import Template # python builtin templater might be used in some utility cases

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir, 'src', 'templates'))

from vehicles import registered_vehicles


class Train(object):
    """Base class for all types of trains"""
    def __init__(self, id, **kwargs):
        self.id = id

        # setup properties for this train
        self.title = kwargs.get('title', None)
        self.numeric_id = kwargs.get('numeric_id', None)
        self.str_type_info = kwargs.get('str_type_info', None).upper()
        self.intro_date = kwargs.get('intro_date', None)
        self.replacement_id = kwargs.get('replacement_id', None)
        self.vehicle_life = kwargs.get('vehicle_life', None)
        self.buy_cost = kwargs.get('buy_cost', None)
        self.fixed_run_cost_factor = kwargs.get('fixed_run_cost_factor', None)
        self.fuel_run_cost_factor = kwargs.get('fuel_run_cost_factor', None)
        self.gross_tonnage = kwargs.get('gross_tonnage', None)
        self.loading_speed = kwargs.get('loading_speed', None)
        self.buy_menu_width = kwargs.get('buy_menu_width', None)
        self.offsets = kwargs.get('offsets', None)
        self.inland_capable = kwargs.get('inland_capable', None)
        self.sea_capable = kwargs.get('sea_capable', None)
        self.speed = kwargs.get('speed', None)
        self.speed_unladen = self.speed * kwargs.get('speed_factor_unladen', None)
        self.ocean_speed = (0.8, 1)[self.sea_capable]
        self.canal_speed = (0.7, 1)[self.inland_capable]
        # declare capacities for pax, mail and freight, as they are needed later for nml switches
        self.capacity_pax = kwargs.get('capacity_pax', 0)
        self.capacity_mail = kwargs.get('capacity_mail', 0)
        self.capacity_freight = kwargs.get('capacity_freight', 0) # over-ride in subclass as needed
        # create a structure to hold model variants
        self.model_variants = []
        # some project management stuff
        self.graphics_status = kwargs.get('graphics_status', None)
        # register vehicle with this module so other modules can use it
        registered_vehicles.append(self)

    def add_model_variant(self, intro_date, end_date, spritesheet_suffix):
        self.model_variants.append(ModelVariant(intro_date, end_date, spritesheet_suffix))

    def get_reduced_set_of_variant_dates(self):
        # find all the unique dates that will need a switch constructing
        years = sorted(reduce(set.union, [(variant.intro_date, variant.end_date) for variant in self.model_variants], set()))
        # quick integrity check
        if years[0] != 0:
            utils.echo_message(self.id + " doesn't have at least one model variant with intro date 0 (required for nml switches to work)")
        return years

    def get_variants_available_for_specific_year(self, year):
        # put the data in a format that's easy to render as switches
        result = []
        for variant in self.model_variants:
            if year in range(variant.intro_date, variant.end_date):
                result.append(variant.spritesheet_suffix)
        return result # could call set() here, but I didn't bother, shouldn't be needed if model variants set up correctly

    def get_nml_random_switch_fragments_for_model_variants(self):
        # return fragments of nml for use in switches
        result = []
        years = self.get_reduced_set_of_variant_dates()
        for index, year in enumerate(years):
            if index < len(years) - 1:
                from_date = year
                until_date = years[index + 1] - 1
                result.append(str(from_date) + '..' + str(until_date) + ':' + self.id + '_switch_graphics_random_' + str(from_date))
        return result

    def get_num_spritesets(self):
        return len(set([i.spritesheet_suffix for i in self.model_variants]))

    def get_speeds_adjusted_for_load_amount(self, speed_index):
        # ships may travel faster or slower than 'speed' depending on cargo amount
        speeds_adjusted = (
            ((self.speed_unladen * 100 + self.speed * 0) * 32 + 9) / 1000,
            ((self.speed_unladen * 75 + self.speed * 25) * 32 + 9) / 1000,
            ((self.speed_unladen * 50 + self.speed * 50) * 32 + 9) / 1000,
            ((self.speed_unladen * 25 + self.speed * 75) * 32 + 9) / 1000,
            ((self.speed_unladen * 0 + self.speed * 100) * 32 + 9) / 1000,
        )
        speed_factors = [0.67, 1, 1.33] # there is a speed adjustment parameter, use that to look up a speed factor
        speeds_adjusted_rounded = [int(math.ceil(i * speed_factors[speed_index])) for i in speeds_adjusted] # allow that integer maths is needed for newgrf cb results; rounding up for safety
        return speeds_adjusted_rounded

    @property
    def adjusted_model_life(self):
        # handles keeping the buy menu tidy, relies on magic from Eddi
        if self.replacement_id != None and self.replacement_id != '-none' and self.replacement_id != '':
            for i in registered_vehicles:
                if i.id == self.replacement_id:
                    model_life = i.intro_date - self.intro_date
                    return model_life + self.vehicle_life
        else:
            return 'VEHICLE_NEVER_EXPIRES'

    @property
    def running_cost(self):
        # calculate a running cost
        fixed_run_cost = self.fixed_run_cost_factor * global_constants.FIXED_RUN_COST
        fuel_run_cost =  self.fuel_run_cost_factor * self.gross_tonnage * global_constants.FUEL_RUN_COST
        calculated_run_cost = int((fixed_run_cost + fuel_run_cost) / 98) # divide by magic constant to get costs as factor in 0-255 range
        return min(calculated_run_cost, 255) # cost factor is a byte, can't exceed 255

    @property
    def refittable_classes(self):
        cargo_classes = []
        # maps lists of allowed classes.  No equivalent for disallowed classes, that's overly restrictive and damages the viability of class-based refitting
        for i in self.class_refit_groups:
            [cargo_classes.append(cargo_class) for cargo_class in global_constants.base_refits_by_class[i]]
        return ','.join(set(cargo_classes)) # use set() here to dedupe

    def get_label_refits_allowed(self):
        # allowed labels, for fine-grained control in addition to classes
        return ','.join(self.label_refits_allowed)

    def get_label_refits_disallowed(self):
        # disallowed labels, for fine-grained control, knocking out cargos that are allowed by classes, but don't fit for gameplay reasons
        return ','.join(self.label_refits_disallowed)

    def get_name_substr(self):
        # relies on name being in format "Foo [Bar]" for Name [Type Suffix]
        return self.title.split('[')[0]

    def get_str_name_suffix(self):
        # used in vehicle name string only, relies on name property value being in format "Foo [Bar]" for Name [Type Suffix]
        type_suffix = self.title.split('[')[1].split(']')[0]
        type_suffix = type_suffix.upper()
        type_suffix = '_'.join(type_suffix.split(' '))
        return 'STR_NAME_SUFFIX_' + type_suffix

    def get_str_type_info(self):
        # makes a string id for nml
        return 'STR_' + self.str_type_info

    def get_name(self):
        return "string(STR_NAME_" + self.id +", string(" + self.get_str_name_suffix() + "))"

    def get_buy_menu_string(self):
        buy_menu_template = Template(
            "string(STR_BUY_MENU_TEXT, string(${str_type_info}), string(STR_EMPTY))"
        )
        return buy_menu_template.substitute(str_type_info=self.get_str_type_info())

    def get_cargo_suffix(self):
        return 'string(' + self.cargo_units_refit_menu + ')'

    def render_debug_info(self):
        template = templates["debug_info.pynml"]
        return template(vehicle=self)

    def render_properties(self):
        template = templates["train_properties.pynml"]
        return template(vehicle=self)

    def render_speed_switches(self):
        template = templates["speed_switches.pynml"]
        return template(vehicle=self)

    def render_autorefit(self):
        template = templates["autorefit_any.pynml"]
        return template(vehicle=self)

    def render_cargo_capacity(self):
        if hasattr(self, 'capacity_is_refittable_by_cargo_subtype'):
            template = templates["capacity_refittable.pynml"]
        else:
            template = templates["capacity_not_refittable.pynml"]
        return template(vehicle=self)

    def render_purchase_cargo_capacity(self):
        template = templates["purchase_cargo_capacity.pynml"]
        return template(vehicle=self)

    def render(self):
        template = templates[self.template]
        return template(vehicle=self, global_constants=global_constants)


class MixinRefittableCapacity(object):
    def capacity_is_refittable_by_cargo_subtype(self):
        return True

    def get_buy_menu_string(self):
        buy_menu_template = Template(
            "string(STR_BUY_MENU_TEXT, string(${str_type_info}), string(STR_GENERIC_REFIT_SUBTYPE_BUY_MENU_INFO,${capacity_0},${capacity_1},${capacity_2},string(${cargo_units})))"
        )
        return buy_menu_template.substitute(str_type_info=self.get_str_type_info(), capacity_0=self.capacities_refittable[0],
                                        capacity_1=self.capacities_refittable[1], capacity_2=self.capacities_refittable[2],
                                        cargo_units=self.cargo_units_buy_menu)


class ModelVariant(object):
    # simple class to hold model variants
    # variants are mostly randomised or date-sensitive graphics
    # must be a minimum of one variant per train
    # at least one variant must have intro date 0 (for nml switch defaults to work)
    def __init__(self, intro_date, end_date, spritesheet_suffix):
        self.intro_date = intro_date
        self.end_date = end_date
        self.spritesheet_suffix = spritesheet_suffix # use digits for these - to match spritesheet filenames


class GeneralCargoVessel(Train):
    """
    General purpose freight vessel type. No pax or mail cargos, refits any other cargo including liquids (in barrels or containers).
    """
    def __init__(self, id, **kwargs):
        super(GeneralCargoVessel, self).__init__(id, **kwargs)
        self.template = 'train.pynml'
        self.class_refit_groups = ['all_freight']
        self.label_refits_allowed = [] # no specific labels needed, GCV refits all freight
        self.label_refits_disallowed = ['TOUR']
        self.capacity_freight = kwargs.get('capacity_cargo_holds', None)
        self.default_cargo = 'COAL'
        self.default_cargo_capacity = self.capacity_freight


class PacketBoat(Train):
    """
    A relatively fast vessel type for passengers, mail, and express freight.
    """
    def __init__(self, id, **kwargs):
        super(PacketBoat, self).__init__(id, **kwargs)
        self.template = 'train.pynml'
        self.class_refit_groups = ['pax_mail','express_freight']
        self.label_refits_allowed = ['BDMT','FRUT','LVST','VEHI','WATR']
        self.label_refits_disallowed = ['FISH'] # don't go fishing with packet boats, use a trawler instead :P
        self.capacity_cargo_holds = kwargs.get('capacity_cargo_holds', 0)
        self.capacity_freight = self.capacity_cargo_holds
        self.default_cargo = 'PASS'
        self.default_cargo_capacity = self.capacity_pax

    def get_buy_menu_string(self):
        # set buy menu text, with various variations
        cargo_units = None # only used when needed
        buy_menu_template = Template(
            "string(STR_BUY_MENU_TEXT, string(${str_type_info}), string(STR_BUY_MENU_REFIT_CAPACITIES_PACKET,${capacity_mail},${capacity_cargo_holds}))"
        )
        return buy_menu_template.substitute(str_type_info=self.get_str_type_info(), capacity_pax=self.capacity_pax,
                                            capacity_mail=self.capacity_mail, capacity_cargo_holds=self.capacity_cargo_holds)


class Hydrofoil(Train):
    """
    Fast vessel type for passengers and mail only, graphics vary by speed (to show hydrofoil in / out of water).
    """
    def __init__(self, id, **kwargs):
        super(Hydrofoil, self).__init__(id, **kwargs)
        self.template = 'hydrofoil.pynml'
        self.class_refit_groups = ['pax_mail']
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.default_cargo = 'PASS'
        self.default_cargo_capacity = self.capacity_pax


class Trawler(Train):
    """
    Similar type to a packet boat, but needs to go fishing, so has special fish holds for that.
    """
    def __init__(self, id, **kwargs):
        super(Trawler, self).__init__(id, **kwargs)
        self.template = 'train.pynml'
        self.class_refit_groups = ['pax_mail','express_freight']
        self.label_refits_allowed = ['BDMT','FISH', 'FRUT','LVST','VEHI','WATR']
        self.label_refits_disallowed = []
        self.capacity_deck_cargo = kwargs.get('capacity_deck_cargo', None)
        self.capacity_freight = self.capacity_deck_cargo
        self.capacity_fish_holds = kwargs.get('capacity_fish_holds', None)
        self.default_cargo = 'FISH'
        self.default_cargo_capacity = self.capacity_fish_holds

    def get_buy_menu_string(self):
        # set buy menu text, with various variations
        cargo_units = None # only used when needed
        buy_menu_template = Template(
                "string(STR_BUY_MENU_TEXT, string(${str_type_info}), string(STR_BUY_MENU_REFIT_CAPACITIES_TRAWLER,${capacity_pax},${capacity_mail},${capacity_fish_holds},${capacity_deck_cargo}))"
        )
        return buy_menu_template.substitute(str_type_info=self.get_str_type_info(), capacity_pax=self.capacity_pax,
                                            capacity_mail=self.capacity_mail, capacity_deck_cargo=self.capacity_deck_cargo,
                                            capacity_fish_holds=self.capacity_fish_holds)
