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
        self.loading_speed = kwargs.get('loading_speed', None)
        self.vehicle_length = kwargs.get('vehicle_length', None)
        self.buy_menu_width = kwargs.get('buy_menu_width', None)
        # offsets can be over-ridden on a per-model basis, or just use the standard ones for vehicle length
        self.offsets = kwargs.get('offsets', global_constants.default_train_offsets[str(self.vehicle_length)])
        self.power = kwargs.get('power', 0)
        self.speed = kwargs.get('speed', 0)
        self.weight = kwargs.get('weight', None)
        self.tractive_effort_coefficient = kwargs.get('tractive_effort_coefficient', 0.3) # 0.3 is recommended default value
        # declare capacities for pax, mail and freight, as they are needed later for nml switches
        self.capacities_pax = self.get_capacity_variations(kwargs.get('capacity_pax', 0))
        self.capacities_mail = self.get_capacity_variations(kwargs.get('capacity_mail', 0))
        self.capacities_freight = self.get_capacity_variations(kwargs.get('capacity_freight', 0))
        # create a structure to hold model variants
        self.model_variants = []
        # set defaults for props otherwise set by subclass as needed (not set by kwargs as specific models do not over-ride them)
        self.default_cargo = 'PASS' # over-ride in subclass as needed (PASS is sane default)
        self.class_refit_groups = []
        self.label_refits_allowed = [] # no specific labels needed
        self.label_refits_disallowed = []
        self.autorefit = False
        self.engine_class = 'ENGINE_CLASS_STEAM' # nml constant (STEAM is sane default)
        self.visual_effect = 'VISUAL_EFFECT_DISABLE' # nml constant
        self.visual_effect_offset = 0
        self.dual_headed = 0
        self.articulated = False
        # some project management stuff
        self.graphics_status = kwargs.get('graphics_status', None)
        # register vehicle with this module so other modules can use it, with a non-blocking guard on duplicate IDs
        # don't register trailing parts, they are taken care of by their parent vehicle
        for vehicle in registered_vehicles:
            if vehicle.numeric_id == self.numeric_id:
                utils.echo_message("Error: vehicle " + self.id + " shares duplicate id (" + str(self.numeric_id) + ") with vehicle " + vehicle.id)
        if not isinstance(self, TrailingPart):
            registered_vehicles.append(self)

    def add_model_variant(self, intro_date, end_date, spritesheet_suffix):
        self.model_variants.append(ModelVariant(intro_date, end_date, spritesheet_suffix))

    def get_id(self, id_base, **kwargs):
        # auto id creator, used for wagons not locos
        return '_'.join((id_base, kwargs['vehicle_set'], 'gen', str(kwargs['wagon_generation'])))

    def get_numeric_id(self, id_base, **kwargs):
        # auto numeric_id creator, used for wagons not locos
        return id_base + (100 * global_constants.vehicle_set_id_mapping[kwargs['vehicle_set']]) + kwargs['wagon_generation']

    def get_trailing_parts(self, id, parent_vehicle, **kwargs):
        trailing_parts = []
        for count, trailing_part_length in enumerate(kwargs['trailing_part_lengths']):
            vehicle_kwargs = kwargs
            trailing_part_id = self.id + '_trailing_part_' + str(count + 1)
            vehicle_kwargs['numeric_id'] = self.numeric_id + count + 1
            trailing_parts.append(TrailingPart(trailing_part_id, parent_vehicle, trailing_part_length, **vehicle_kwargs))
        return trailing_parts

    def get_capacity_variations(self, capacity):
        # capacity is variable, controlled by a newgrf parameter 
        # we cache the available variations on the vehicle instead of working them out every time - easier 
        # allow that integer maths is needed for newgrf cb results; round up for safety
        return [int(math.ceil(capacity * multiplier)) for multiplier in global_constants.capacity_multipliers]

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
    def availability(self):
        # which climates vehicle is available in
        if isinstance(self, TrailingPart):
            return "NO_CLIMATE"
        else:
            return "ALL_CLIMATES"

    @property
    def special_flags(self):
        special_flags = ['TRAIN_FLAG_2CC']
        if self.autorefit == True:
            special_flags.append('TRAIN_FLAG_AUTOREFIT')
        return ','.join(special_flags)

    @property
    def running_cost(self):
        # calculate a running cost
        fixed_run_cost = self.fixed_run_cost_factor * global_constants.FIXED_RUN_COST
        fuel_run_cost =  self.fuel_run_cost_factor * global_constants.FUEL_RUN_COST
        calculated_run_cost = int((fixed_run_cost + fuel_run_cost) / 98) # divide by magic constant to get costs as factor in 0-255 range
        return min(calculated_run_cost, 255) # cost factor is a byte, can't exceed 255

    @property
    def capacity_pax(self):
        return self.capacities_pax[0]
    @property
    
    def capacity_mail(self):
        return self.capacities_mail[0]
    
    @property
    def capacity_freight(self):
        return self.capacities_freight[0]

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
        if isinstance(self, TrailingPart):
            return "string(STR_EMPTY)"
        else:
            return "string(STR_NAME_" + self.id +", string(" + self.get_str_name_suffix() + "))"

    def get_buy_menu_string(self):
        buy_menu_template = Template(
            "string(STR_BUY_MENU_TEXT, string(${str_type_info}), string(STR_EMPTY))"
        )
        return buy_menu_template.substitute(str_type_info=self.get_str_type_info())

    def get_cargo_suffix(self):
        return 'string(' + self.cargo_units_refit_menu + ')'
        
    def assert_cargo_labels(self, cargo_labels):
        for i in cargo_labels:
            if i not in global_constants.cargo_labels:
                utils.echo_message("Warning: vehicle " + self.id + " references cargo label " + i + " which is not defined in the cargo table")                

    def render_debug_info(self):
        template = templates["debug_info.pynml"]
        return template(vehicle=self)

    def render_properties(self):
        template = templates["train_properties.pynml"]
        return template(vehicle=self)

    def render_cargo_capacity(self):
        template = templates["capacity_switches.pynml"]
        return template(vehicle=self)

    def render(self):
        # integrity tests
        self.assert_cargo_labels(self.label_refits_allowed)
        self.assert_cargo_labels(self.label_refits_disallowed)
        # templating
        template = templates[self.template]
        nml_result = template(vehicle=self, global_constants=global_constants)
        if self.articulated:
            for trailing_part in self.trailing_parts:
                nml_result = trailing_part.render() + nml_result
        return nml_result


class ModelVariant(object):
    # simple class to hold model variants
    # variants are mostly randomised or date-sensitive graphics
    # must be a minimum of one variant per train
    # at least one variant must have intro date 0 (for nml switch defaults to work)
    def __init__(self, intro_date, end_date, spritesheet_suffix):
        self.intro_date = intro_date
        self.end_date = end_date
        self.spritesheet_suffix = spritesheet_suffix # use digits for these - to match spritesheet filenames


class TrailingPart(Train):
    """
    Trailing part for articulated (not dual-headed) vehicles.
    """
    def __init__(self, id, parent_vehicle, trailing_part_length, **kwargs):
        kwargs['vehicle_length'] = trailing_part_length
        super(TrailingPart, self).__init__(id, **kwargs)
        self.title = 'Trailing Part []'
        self.template = 'trailing_part.pynml'
        self.speed = 0
        self.weight = 0
        self.default_cargo_capacities = [0]
        self.parent_vehicle = parent_vehicle
        self.model_variants = parent_vehicle.model_variants


class Wagon(Train):
    """
    Intermediate class for actual cars (wagons) to subclass from, provides some common properties.
    This class should be sparse - only declare the most limited set of properties common to wagons.
    Most props should be declared by Train with useful defaults, or by the subclass providing the car.
    """
    def __init__(self, id, speedy=False, **kwargs):
        super(Wagon, self).__init__(id, **kwargs)
        self.wagon_generation = kwargs.get('wagon_generation', None)
        if self.wagon_generation == 1:
            if speedy==True:
                self.speed = global_constants.speedy_wagon_speed
            else:
                self.speed = global_constants.standard_wagon_speed


class SteamTankLoco(Train):
    """
    Steam Tank Locomotive.
    """
    def __init__(self, id, **kwargs):
        super(SteamTankLoco, self).__init__(id, **kwargs)
        self.template = 'train.pynml'
        self.default_cargo_capacities = [0]
        self.engine_class = 'ENGINE_CLASS_STEAM' #nml constant
        self.visual_effect = 'VISUAL_EFFECT_STEAM' # nml constant


class SteamTenderLoco(Train):
    """
    Steam Tender Locomotive.
    """
    def __init__(self, id, **kwargs):
        super(SteamTenderLoco, self).__init__(id, **kwargs)
        self.template = 'train.pynml'
        self.default_cargo_capacities = [0]
        self.engine_class = 'ENGINE_CLASS_STEAM' #nml constant
        self.visual_effect = 'VISUAL_EFFECT_STEAM' # nml constant
        self.articulated = True
        self.trailing_parts = self.get_trailing_parts(id, self, **kwargs)


class DieselLoco(Train):
    """
    Diesel Locomotive.
    """
    def __init__(self, id, **kwargs):
        super(DieselLoco, self).__init__(id, **kwargs)
        self.template = 'train.pynml'
        self.default_cargo_capacities = [0]
        self.engine_class = 'ENGINE_CLASS_DIESEL' #nml constant
        self.visual_effect = 'VISUAL_EFFECT_DIESEL' # nml constant


class DieselMultipleUnit(Train):
    """
    Diesel Multiple Unit.
    """
    def __init__(self, id, **kwargs):
        super(DieselMultipleUnit, self).__init__(id, **kwargs)
        self.template = 'train.pynml'
        self.default_cargo_capacities = [0]
        self.engine_class = 'ENGINE_CLASS_DIESEL' #nml constant
        self.visual_effect = 'VISUAL_EFFECT_DIESEL' # nml constant
        self.dual_headed = 1


class ElectricLoco(Train):
    """
    Diesel Locomotive.
    """
    def __init__(self, id, **kwargs):
        super(ElectricLoco, self).__init__(id, **kwargs)
        self.template = 'train.pynml'
        self.default_cargo_capacities = [0]
        self.engine_class = 'ENGINE_CLASS_ELECTRIC' #nml constant
        self.visual_effect = 'VISUAL_EFFECT_ELECTRIC' # nml constant


class ElectricMultipleUnit(Train):
    """
    Electric Multiple Unit.
    """
    def __init__(self, id, **kwargs):
        super(ElectricMultipleUnit, self).__init__(id, **kwargs)
        self.template = 'train.pynml'
        self.default_cargo_capacities = [0]
        self.engine_class = 'ENGINE_CLASS_ELECTRIC' #nml constant
        self.visual_effect = 'VISUAL_EFFECT_ELECTRIC' # nml constant
        self.dual_headed = 1


class PassengerCar(Wagon):
    """
    Passenger Carriage.
    """
    def __init__(self, **kwargs):
        id = self.get_id('passenger_car', **kwargs)
        super(PassengerCar, self).__init__(id, speedy=True, **kwargs)
        self.numeric_id = self.get_numeric_id(10000, **kwargs)
        self.template = 'train.pynml'
        self.class_refit_groups = ['pax']
        self.label_refits_allowed = [] # no specific labels needed
        self.label_refits_disallowed = []
        self.autorefit = True
        self.default_cargo = 'PASS'
        self.default_cargo_capacities = self.capacities_pax


class MailCar(Wagon):
    """
    Mail Carriage.
    """
    def __init__(self, **kwargs):
        id = self.get_id('mail_car', **kwargs)
        super(MailCar, self).__init__(id, speedy=True, **kwargs)
        self.numeric_id = self.get_numeric_id(11000, **kwargs)
        self.template = 'train.pynml'
        self.class_refit_groups = ['mail', 'express_freight']
        self.label_refits_allowed = [] # no specific labels needed
        self.label_refits_disallowed = []
        self.autorefit = True
        self.capacities_freight = [int(0.5 * capacity) for capacity in self.capacities_mail]
        self.default_cargo_capacities = self.capacities_mail
        self.default_cargo = 'MAIL'


class CabooseCar(Wagon):
    """
    Caboose (Brake Van).
    """
    def __init__(self, **kwargs):
        id = self.get_id('caboose_car', **kwargs)
        super(CabooseCar, self).__init__(id, **kwargs)
        self.numeric_id = self.get_numeric_id(20000, **kwargs)
        self.template = 'train.pynml'
        self.default_cargo_capacities = [0]
        self.loading_speed = 0
        self.speed = 0


class BoxCar(Wagon):
    """
    Boxcar.
    """
    def __init__(self, **kwargs):
        id = self.get_id('box_car', **kwargs)
        super(BoxCar, self).__init__(id, **kwargs)
        self.numeric_id = self.get_numeric_id(12000, **kwargs)
        self.template = 'train.pynml'
        self.class_refit_groups = ['packaged_freight']
        self.label_refits_allowed = ['GRAI', 'WHEA', 'MAIZ'] # no specific labels needed
        self.label_refits_disallowed = []
        self.autorefit = True
        self.default_cargo = 'GOOD'
        self.default_cargo_capacities = self.capacities_freight


class HopperCar(Wagon):
    """
    Hopper Car.
    """
    def __init__(self, **kwargs):
        id = self.get_id('hopper_car', **kwargs)
        super(HopperCar, self).__init__(id, **kwargs)
        self.numeric_id = self.get_numeric_id(13000, **kwargs)
        self.template = 'train.pynml'
        self.class_refit_groups = ['hopper_freight']
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.autorefit = True
        self.default_cargo = 'COAL'
        self.default_cargo_capacities = self.capacities_freight


class OpenCar(Wagon):
    """
    Open Car (Gondola).
    """
    def __init__(self, **kwargs):
        id = self.get_id('open_car', **kwargs)
        super(OpenCar, self).__init__(id, **kwargs)
        self.numeric_id = self.get_numeric_id(14000, **kwargs)
        self.template = 'car_with_visible_cargo.pynml'
        self.class_refit_groups = ['all_freight']
        self.num_cargo_rows = 15
        # mappings are to rows in the spritesheet, 0-based (0 is also default)
        # also get the allowed label refits from the graphics mapping - use row 0 if there's no specific graphics for the label 
        self.cargo_graphics_mappings = {'AORE': 1, 'COAL': 2, 'SAND': 3, 'CORE': 4, 'LIME': 5, 
                                        'SCMT': 6, 'IORE': 7, 'GRVL': 8, 'GRAI': 10, 'WHEA': 10,
                                        'MAIZ': 10, 'FICR': 11, 'SGCN': 11, 'OLSD': 12, 'CLAY': 13,
                                        'FRUT': 14, 'FRVG': 14}
        self.label_refits_allowed = self.cargo_graphics_mappings.keys() 
        self.label_refits_disallowed = []
        self.autorefit = True
        self.default_cargo = 'GOOD'
        self.default_cargo_capacities = self.capacities_freight


class TankCar(Wagon):
    """
    Tank Car.
    """
    def __init__(self, **kwargs):
        id = self.get_id('tank_car', **kwargs)
        super(TankCar, self).__init__(id, **kwargs)
        self.numeric_id = self.get_numeric_id(15000, **kwargs)
        self.template = 'tank_car.pynml'
        self.class_refit_groups = ['liquids']
        self.num_cargo_rows = 3
        # mappings are to rows in the spritesheet, 0-based (0 is also default)
        # also get the allowed label refits from the graphics mapping - use row 0 if there's no specific graphics for the label 
        self.cargo_graphics_mappings = {'FMSP': 1, 'MILK': 2, 'RFPR': 1}
        self.label_refits_allowed = self.cargo_graphics_mappings.keys() 
        self.label_refits_disallowed = []
        self.default_cargo = 'OIL_'
        self.default_cargo_capacities = self.capacities_freight


class LivestockCar(Wagon):
    """
    Livestock Car (Gondola).
    """
    def __init__(self, **kwargs):
        id = self.get_id('livestock_car', **kwargs)
        super(LivestockCar, self).__init__(id, **kwargs)
        self.numeric_id = self.get_numeric_id(16000, **kwargs)
        self.template = 'train.pynml'
        self.class_refit_groups = []
        self.label_refits_allowed = ['LVST'] # no specific labels needed
        self.label_refits_disallowed = []
        self.default_cargo = 'LVST'
        self.default_cargo_capacities = self.capacities_freight


class CoveredHopperCar(Wagon):
    """
    Covered Hopper Car.
    """
    def __init__(self, **kwargs):
        id = self.get_id('covered_hopper_car', **kwargs)
        super(CoveredHopperCar, self).__init__(id, **kwargs)
        self.numeric_id = self.get_numeric_id(17000, **kwargs)
        self.template = 'train.pynml'
        self.class_refit_groups = ['covered_hopper_freight']
        self.label_refits_allowed = ['GRAI']
        self.label_refits_disallowed = []
        self.default_cargo = 'GRAI'
        self.default_cargo_capacities = self.capacities_freight


class ReeferCar(Wagon):
    """
    Reefer (Refrigerated) Car.
    """
    def __init__(self, **kwargs):
        id = self.get_id('reefer_car', **kwargs)
        super(ReeferCar, self).__init__(id, **kwargs)
        self.numeric_id = self.get_numeric_id(18000, **kwargs)
        self.template = 'train.pynml'
        self.class_refit_groups = ['refrigerated_freight']
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.autorefit = True
        self.default_cargo = 'FOOD'
        self.default_cargo_capacities = self.capacities_freight


class FlatCar(Wagon):
    """
    Flat Car.
    """
    def __init__(self, **kwargs):
        id = self.get_id('flat_car', **kwargs)
        super(FlatCar, self).__init__(id, **kwargs)
        self.numeric_id = self.get_numeric_id(19000, **kwargs)
        self.template = 'train.pynml'
        self.class_refit_groups = ['flatcar_freight']
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.autorefit = True
        self.default_cargo = 'GOOD'
        self.default_cargo_capacities = self.capacities_freight
