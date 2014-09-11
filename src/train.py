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

import graphics_processor

from rosters import registered_rosters
from vehicles import registered_consists, registered_wagon_generations

import inspect

class Consist(object):
    """
       'Vehicles' (appearing in buy menu) are composed as articulated consists.
       Each consist comprises one or more 'units' (visible).
       Each unit assembled from 3 'slices' (invisible-visible-invisible), which are newgrf vehicles with uids.
   """
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.vehicle_module_path = inspect.stack()[2][1]
        # setup properties for this consist (props either shared for all vehicles, or placed on lead vehicle of consist)
        self.title = kwargs.get('title', None)
        self.base_numeric_id = kwargs.get('base_numeric_id', None)
        self.str_type_info = kwargs.get('str_type_info', None)
        self.intro_date = kwargs.get('intro_date', None)
        self.replacement_id = kwargs.get('replacement_id', None)
        self.vehicle_life = kwargs.get('vehicle_life', None)
        self.power = kwargs.get('power', 0)
        self.track_type = kwargs.get('track_type', 'RAIL')
        self.power_by_tracktype = kwargs.get('power_by_tracktype', None) # used by multi-mode engines such as electro-diesel, otherwise ignored
        self.tractive_effort_coefficient = kwargs.get('tractive_effort_coefficient', 0.3) # 0.3 is recommended default value
        self.speed = kwargs.get('speed', None)
        # arbitrary adjustments of points that can be applied to adjust buy cost and running cost, over-ride in consist as needed
        # values can be -ve or +ve to dibble specific vehicles (but total calculated points cannot exceed 255)
        self.type_base_buy_cost_points = kwargs.get('type_base_buy_cost_points', 15)
        self.type_base_running_cost_points = kwargs.get('type_base_running_cost_points', 15)
        # hangover from switching to 10/8 spritesheet and not wanting to fix existing spritesheets
        self.use_legacy_spritesheet = kwargs.get('use_legacy_spritesheet', False)
        # create a structure to hold model variants
        self.model_variants = []
        # create structure to hold the slices
        self.slices = []
        # some project management stuff
        self.graphics_status = kwargs.get('graphics_status', None)
        # register consist with this module so other modules can use it, with a non-blocking guard on duplicate IDs
        for consist in registered_consists:
            if consist.base_numeric_id == self.base_numeric_id:
                utils.echo_message("Error: consist " + self.id + " shares duplicate id (" + str(self.base_numeric_id) + ") with consist " + consist.id)
        registered_consists.append(self)

    def add_model_variant(self, intro_date, end_date, spritesheet_suffix, graphics_processor=None):
        self.model_variants.append(ModelVariant(intro_date, end_date, spritesheet_suffix, graphics_processor))

    def add_unit(self, vehicle, repeat=1):
        # vehicle ids increment by 3 because each vehicle is composed of 3 intermediate slices
        count = len(set(self.slices))
        first_slice = LeadSlice(parent_vehicle=vehicle)
        second_slice = vehicle
        third_slice = NullTrailingSlice(parent_vehicle=vehicle)
        if count == 0:
            first_slice.id = self.id # first vehicle gets no numeric id suffix - for compatibility with buy menu list ids etc
        else:
            first_slice.id = self.id + '_' + str(count)
        second_slice.id = self.id + '_' + str(count + 1)
        third_slice.id = self.id + '_' + str(count + 2)
        first_slice.numeric_id = self.get_and_verify_numeric_id(count)
        second_slice.numeric_id = self.get_and_verify_numeric_id(count + 1)
        third_slice.numeric_id = self.get_and_verify_numeric_id(count + 2)
        first_slice.slice_length = global_constants.slice_lengths[vehicle.vehicle_length][0]
        second_slice.slice_length = global_constants.slice_lengths[vehicle.vehicle_length][1]
        third_slice.slice_length = global_constants.slice_lengths[vehicle.vehicle_length][2]
        first_slice.spriterow_num = vehicle.spriterow_num

        for repeat_num in range(repeat):
            self.slices.append(first_slice)
            self.slices.append(second_slice)
            self.slices.append(third_slice)

    def get_and_verify_numeric_id(self, offset):
        numeric_id = self.base_numeric_id + offset
        # guard against the ID being too large to build in an articulated consist
        if numeric_id > 16383:
            utils.echo_message("Error: numeric_id " + str(numeric_id) + " for " + self.id + " can't be used (16383 is max ID for articulated vehicles)")
        # guard against ID collisions with other vehicles
        for consist in registered_consists:
            for slice in consist.slices:
                if numeric_id == slice.numeric_id:
                    utils.echo_message("Error: numeric_id collision (" + str(numeric_id) + ") for slices in consist " + self.id + " and " + consist.id)
        return numeric_id

    def get_wagon_id(self, id_base, **kwargs):
        # auto id creator, used for wagons not locos
        return '_'.join((id_base, kwargs['vehicle_set'], 'gen', str(kwargs['wagon_generation'])))

    def get_wagon_numeric_id(self, base_id, **kwargs):
        # auto numeric_id creator, used for wagons not locos
        vehicle_set_base_number = global_constants.vehicle_set_id_mapping[kwargs['vehicle_set']]
        type_base_number = global_constants.wagon_type_numeric_ids[base_id]
        result = (1000 * vehicle_set_base_number) + type_base_number + (3 * (kwargs['wagon_generation'] - 1))
        return result

    def get_reduced_set_of_variant_dates(self):
        # find all the unique dates that will need a switch constructing
        years = sorted(reduce(set.union, [(variant.intro_date, variant.end_date) for variant in self.model_variants], set()))
        # quick integrity check
        if years[0] != 0:
            utils.echo_message(self.id + " doesn't have at least one model variant with intro date 0 (required for nml switches to work)")
        return years

    def get_num_spritesets(self):
        return len(set([i.spritesheet_suffix for i in self.model_variants]))

    def get_variants_available_for_specific_year(self, year):
        # put the data in a format that's easy to render as switches
        result = []
        for variant in self.model_variants:
            if year in range(variant.intro_date, variant.end_date):
                result.append(variant.spritesheet_suffix)
        return result # could call set() here, but I didn't bother, shouldn't be needed if model variants set up correctly

    def get_nml_random_switch_fragments_for_model_variants(self, vehicle):
        # return fragments of nml for use in switches
        result = []
        years = self.get_reduced_set_of_variant_dates()
        for index, year in enumerate(years):
            if index < len(years) - 1:
                from_date = year
                until_date = years[index + 1] - 1
                result.append(str(from_date) + '..' + str(until_date) + ':' + vehicle.id + '_switch_graphics_random_' + str(from_date))
        return result

    def get_name_substr(self):
        # relies on name being in format "Foo [Bar]" for Name [Type Suffix]
        return self.title.split('[')[0]

    def get_str_name_suffix(self):
        # used in vehicle name string only, relies on name property value being in format "Foo [Bar]" for Name [Type Suffix]
        type_suffix = self.title.split('[')[1].split(']')[0]
        type_suffix = type_suffix.upper()
        type_suffix = '_'.join(type_suffix.split(' '))
        return 'STR_NAME_SUFFIX_' + type_suffix

    def get_str_cargo_age_period(self):
        for slice in self.slices:
            if getattr(slice, 'cargo_age_period', global_constants.CARGO_AGE_PERIOD) > global_constants.CARGO_AGE_PERIOD:
                return 'STR_BUY_MENU_IMPROVED_CARGO_AGE_PERIOD'
        return 'STR_EMPTY'

    def get_str_autorefit(self):
        if self.any_slice_offers_autorefit():
            return 'STR_BUY_MENU_OFFERS_AUTOREFIT'
        else:
            return 'STR_EMPTY'

    def get_name(self):
        return "string(STR_NAME_" + self.id +", string(" + self.get_str_name_suffix() + "))"

    def get_buy_menu_string(self):
        # will need to handle bi-mode locos here, have a look at consist.slice_requires_variable_power(vehicle)
        # buy menu handling could be refactored - construct by appending each item as needed (provide 'type:' string as a substr)
        buy_menu_template = Template(
            "string(STR_BUY_MENU_TEXT, string(${str_autorefit}), string(${str_cargo_age_period}))"
        )
        return buy_menu_template.substitute(str_autorefit=self.get_str_autorefit(),
                                            str_cargo_age_period=self.get_str_cargo_age_period())

    def any_slice_offers_autorefit(self):
        offers_autorefit = False
        for slice in self.slices:
            if getattr(slice, 'autorefit', False):
                offers_autorefit = True
        return offers_autorefit

    def slice_requires_variable_power(self, vehicle):
        if self.power_by_tracktype is not None and vehicle.is_lead_slice_of_consist:
            return True
        else:
            return False

    @property
    def buy_cost(self):
        # stub only
        # vehicle classes should over-ride this to provide class-appropriate cost calculation
        return 0

    @property
    def running_cost(self):
        # stub only
        # vehicle classes should over-ride this to provide class-appropriate running cost calculation
        return 0

    @property
    def weight(self):
        return sum([getattr(slice, 'weight', 0) for slice in self.slices])

    @property
    def adjusted_model_life(self):
        # handles keeping the buy menu tidy, relies on magic from Eddi
        if self.replacement_id != None and self.replacement_id != '-none' and self.replacement_id != '':
            for i in registered_consists:
                if i.id == self.replacement_id:
                    model_life = i.intro_date - self.intro_date
                    return model_life + self.vehicle_life
        else:
            return 'VEHICLE_NEVER_EXPIRES'

    @property
    def buy_menu_width (self):
        # max sensible width in buy menu is 64px
        consist_length = 4 * sum([slice.slice_length for slice in self.slices])
        if consist_length < 64:
            return consist_length
        else:
            return 64

    def render_debug_info(self):
        template = templates["debug_info_consist.pynml"]
        return template(consist=self)

    def render_articulated_switch(self):
        template = templates["add_articulated_parts.pynml"]
        nml_result = template(consist=self, global_constants=global_constants)
        return nml_result

    def render_dummy(self):
        template = templates["dummy.pynml"]
        nml_result = template(consist=self, global_constants=global_constants, utils=utils)
        return nml_result

    def render(self):
        # templating
        print('Rendering ' + self.id)
        nml_result = ''
        nml_result = nml_result + self.render_dummy() # do this first so we can split it off cleanly
        nml_result = nml_result + self.render_articulated_switch()
        for slice in set(self.slices):
            nml_result = nml_result + slice.render()
        return nml_result


class Train(object):
    """Base class for all types of trains"""
    def __init__(self, **kwargs):
        self.consist = kwargs.get('consist')

        # setup properties for this train
        self.numeric_id = kwargs.get('numeric_id', None)
        self.loading_speed = kwargs.get('loading_speed', 5) # 5 is default train loading speed
        self.cargo_age_period = kwargs.get('cargo_age_period', global_constants.CARGO_AGE_PERIOD)
        self.vehicle_length = kwargs.get('vehicle_length', None)
        self.speed = kwargs.get('speed', 0)
        self.weight = kwargs.get('weight', None)
        # declare capacities for pax, mail and freight, as they are needed later for nml switches
        self.capacities_pax = self.get_capacity_variations(kwargs.get('capacity_pax', 0))
        self.capacities_mail = self.get_capacity_variations(kwargs.get('capacity_mail', 0))
        self.capacities_freight = self.get_capacity_variations(kwargs.get('capacity_freight', 0))
        # spriterow_num, first row = 0
        self.spriterow_num = kwargs.get('spriterow_num', 0)
        # set defaults for props otherwise set by subclass as needed (not set by kwargs as specific models do not over-ride them)
        self.default_cargo = 'PASS' # over-ride in subclass as needed
        self.class_refit_groups = []
        self.label_refits_allowed = [] # no specific labels needed
        self.label_refits_disallowed = []
        self.autorefit = False
        self.engine_class = 'ENGINE_CLASS_STEAM' # nml constant (STEAM is sane default)
        self.visual_effect = 'VISUAL_EFFECT_DISABLE' # nml constant
        self.visual_effect_offset = 0

    def get_capacity_variations(self, capacity):
        # capacity is variable, controlled by a newgrf parameter
        # we cache the available variations on the vehicle instead of working them out every time - easier
        # allow that integer maths is needed for newgrf cb results; round up for safety
        return [int(math.ceil(capacity * multiplier)) for multiplier in global_constants.capacity_multipliers]

    @property
    def availability(self):
        # only show vehicle in buy menu if it is first vehicle in consist
        if self.is_lead_slice_of_consist:
            return "ALL_CLIMATES"
        else:
            return "NO_CLIMATE"

    @property
    def is_lead_slice_of_consist(self):
        # first slice in the complete multi-unit consist
        if self.numeric_id == self.consist.base_numeric_id:
            return True
        else:
            return False

    @property
    def is_lead_slice_of_unit(self):
        # first slice in a unit
        return isinstance(self, LeadSlice)

    @property
    def special_flags(self):
        special_flags = ['TRAIN_FLAG_2CC']
        if self.autorefit == True:
            special_flags.append('TRAIN_FLAG_AUTOREFIT')
        return ','.join(special_flags)

    @property
    def refittable_classes(self):
        cargo_classes = []
        # maps lists of allowed classes.  No equivalent for disallowed classes, that's overly restrictive and damages the viability of class-based refitting
        for i in self.class_refit_groups:
            [cargo_classes.append(cargo_class) for cargo_class in global_constants.base_refits_by_class[i]]
        return ','.join(set(cargo_classes)) # use set() here to dedupe

    @property
    def running_cost_base(self):
        return {'ENGINE_CLASS_STEAM': 'RUNNING_COST_STEAM',
                           'ENGINE_CLASS_DIESEL': 'RUNNING_COST_DIESEL',
                           'ENGINE_CLASS_ELECTRIC': 'RUNNING_COST_ELECTRIC'}[self.engine_class]

    @property
    def offsets(self):
        # offsets can also be over-ridden on a per-model basis by providing this property in the model class
        return global_constants.default_train_offsets[str(self.vehicle_length)]

    @property
    def location_of_random_bits(self):
        if isinstance(self, LeadSlice):
            return 'SELF'
        else:
            return 'FORWARD_SELF(1)'

    @property
    def sg_depot(self):
        if isinstance(self, LeadSlice):
            suffix = "_switch_graphics_by_year"
        else:
            suffix = "_sg_hidden"
        return self.id + suffix

    @property
    def adjust_xoffs(self):
        # used to correct depot view x offset
        if isinstance(self, LeadSlice):
            return global_constants.xoffs_adjusts[str(self.vehicle_length)]
        else:
            return 0

    @property
    def sg_default(self):
        if isinstance(self, LeadSlice):
            suffix = "_sg_hidden"
        else:
            suffix = "_switch_graphics_by_year"
        return self.id + suffix

    def get_nml_expression_for_cargo_type_unit_refitted_to(self):
        expression_template = Template("[STORE_TEMP(${offset}, 0x10F), var[0x61, 0, 0x000000FF, 0x47]]")
        # cargo capacity is on the second slice of each 3-slice unit
        if isinstance(self, LeadSlice):
            return expression_template.substitute(offset=1)
        else:
            return expression_template.substitute(offset=0)

    def get_nml_expression_for_grfid_of_neighbouring_unit(self, unit_offset):
        # offset is number of units, not number of slices
        expression_template = Template("[STORE_TEMP(${offset}, 0x10F), var[0x61, 0, 0xFFFFFFFF, 0x25]]")
        return expression_template.substitute(offset=(3 * unit_offset))

    def get_nml_expression_for_id_of_neighbouring_unit(self, unit_offset):
        # offset is number of units, not number of slices
        expression_template = Template("[STORE_TEMP(${offset}, 0x10F), var[0x61, 0, 0x0000FFFF, 0xC6]]")
        return expression_template.substitute(offset=(3 * unit_offset))

    def get_label_refits_allowed(self):
        # allowed labels, for fine-grained control in addition to classes
        return ','.join(self.label_refits_allowed)

    def get_label_refits_disallowed(self):
        # disallowed labels, for fine-grained control, knocking out cargos that are allowed by classes, but don't fit for gameplay reasons
        return ','.join(self.label_refits_disallowed)

    def get_cargo_suffix(self):
        return 'string(' + self.cargo_units_refit_menu + ')'

    def assert_cargo_labels(self, cargo_labels):
        for i in cargo_labels:
            if i not in global_constants.cargo_labels:
                utils.echo_message("Warning: vehicle " + self.id + " references cargo label " + i + " which is not defined in the cargo table")

    def render_debug_info(self):
        template = templates["debug_info_vehicle.pynml"]
        return template(vehicle=self)

    def render_properties(self):
        template = templates["train_properties.pynml"]
        return template(vehicle=self, consist=self.consist, global_constants=global_constants)

    def render_cargo_capacity(self):
        template = templates["capacity_switches.pynml"]
        return template(vehicle=self)

    def render(self):
        # integrity tests
        self.assert_cargo_labels(self.label_refits_allowed)
        self.assert_cargo_labels(self.label_refits_disallowed)
        # templating
        template_name = self.template
        template = templates[template_name]
        nml_result = template(vehicle=self, consist=self.consist, global_constants=global_constants)
        return nml_result


class TypeConfig(object):
    # simple class to hold properties common to all instances of a type of vehicle
    # examples of types: Box Car, Steam Engine, Passenger Car etc.
    # declared once per type
    # passed to the type's consists and units
    def __init__(self, base_id, template, **kwargs):
        self.base_id = base_id
        self.template = template
        self.track_type = kwargs.get('track_type', 'RAIL')
        self.num_cargo_rows = kwargs.get('num_cargo_rows', None)
        self.generic_cargo_rows = kwargs.get('generic_cargo_rows', [0]) # optional, the rows to use if no cargo label is matched
        self.cargo_graphics_mappings = kwargs.get('cargo_graphics_mappings', None)
        self.class_refit_groups = kwargs.get('class_refit_groups', None)
        self.label_refits_allowed = kwargs.get('label_refits_allowed', None)
        self.label_refits_disallowed = kwargs.get('label_refits_disallowed', None)
        self.autorefit = kwargs.get('autorefit', None)
        self.default_cargo = kwargs['default_cargo'] # don't use 'get()' - needs to be defined to avoid unwanted refit issues
        self.default_capacity_type = kwargs.get('default_capacity_type', None)
        self.cargo_age_period = kwargs.get('cargo_age_period', global_constants.CARGO_AGE_PERIOD)
        self.str_type_info = kwargs.get('str_type_info', None)


class ModelVariant(object):
    # simple class to hold model variants
    # variants are mostly randomised or date-sensitive graphics
    # must be a minimum of one variant per train
    # at least one variant must have intro date 0 (for nml switch defaults to work)
    def __init__(self, intro_date, end_date, spritesheet_suffix, graphics_processor):
        self.intro_date = intro_date
        self.end_date = end_date
        self.spritesheet_suffix = spritesheet_suffix # use digits for these - to match spritesheet filenames
        self.graphics_processor = graphics_processor

    def get_spritesheet_name(self, consist):
        return consist.id + '_' + str(self.spritesheet_suffix) + '.png'


class GraphicsProcessorFactory(object):
    # simple class which wraps graphics_processor, which uses pixa library
    # pipeline_name refers to a pipeline class which defines how the processing is done
    # may be reused across consists, so don't store consist info in the pipeline, pass it to pipeline at render time
    # this is kind of factory-pattern-ish, but don't make too much of that, it's not important
    def __init__(self, pipeline_name, options):
        self.pipeline_name = pipeline_name
        self.options = options
        self.pipeline = graphics_processor.registered_pipelines[pipeline_name]


class LeadSlice(Train):
    """
    Lead slice for a unit (invisible, minimal props).
    """
    def __init__(self, parent_vehicle):
        super(LeadSlice, self).__init__(consist=parent_vehicle.consist,
                                       loading_speed=parent_vehicle.loading_speed)
        self.parent_vehicle = parent_vehicle
        self.template = parent_vehicle.template
        self.speed = 0
        self.weight = 0
        self.vehicle_length = parent_vehicle.vehicle_length
        self.engine_class = parent_vehicle.engine_class
        self.visual_effect = parent_vehicle.visual_effect
        self.visual_effect_offset = parent_vehicle.visual_effect_offset
        self.default_cargo = parent_vehicle.default_cargo # breaks auto-replace if omitted
        # provide default capacity (set as property) so leads vehicle has same refittability as trailing slices, this prevents an issue with auto-refit
        self.default_cargo_capacities = [1]
        # actual capacity determined by cb checking cargo type, set all of these to 0
        self.capacities_pax = [0, 0, 0]
        self.capacities_freight = [0, 0, 0]
        self.capacities_mail = [0, 0, 0]
        # copy the refittability info from parent
        self.class_refit_groups = parent_vehicle.class_refit_groups
        self.label_refits_allowed = parent_vehicle.label_refits_allowed
        self.label_refits_disallowed = parent_vehicle.label_refits_disallowed
        self.cargo_age_period = parent_vehicle.cargo_age_period
        self.autorefit = parent_vehicle.autorefit
        if isinstance(parent_vehicle, CombineCar):
            self.capacities_pax = parent_vehicle.capacities_pax
            self.default_cargo_capacities = self.capacities_pax
            self.default_cargo = 'PASS'
            self.class_refit_groups = ['pax']


class NullTrailingSlice(object):
    """
    Trailing slice for a unit (invisible, minimal props).
    """
    def __init__(self, parent_vehicle):
        self.id = global_constants.null_trailing_slice_id
        self.numeric_id = global_constants.null_trailing_slice_numeric_id
        # provide default capacity (set as property) so leads vehicle has same refittability as trailing slices, this prevents an issue with auto-refit
        self.default_cargo_capacities = [1]
        # set a bunch of props to default / zero values
        self.capacities_pax = [0, 0, 0]
        self.capacities_freight = [0, 0, 0]
        self.capacities_mail = [0, 0, 0]
        self.default_cargo = parent_vehicle.default_cargo
        # copy the refittability info from parent
        self.class_refit_groups = parent_vehicle.class_refit_groups
        self.label_refits_allowed = parent_vehicle.label_refits_allowed
        self.label_refits_disallowed = parent_vehicle.label_refits_disallowed
        self.cargo_age_period = parent_vehicle.cargo_age_period
        self.autorefit = parent_vehicle.autorefit

    def render(self):
        template = templates['null_trailing_slice.pynml']
        return template(vehicle=self, global_constants=global_constants)


class EngineConsist(Consist):
    """
    Intermediate class for engine consists to subclass from, provides some common properties.
    This class should be sparse - only declare the most limited set of properties common to engine consists.
    """
    def __init__(self, **kwargs):
        id = kwargs.get('id', None)
        super(EngineConsist, self).__init__(**kwargs)

    def get_engine_cost_points(self):
        # Up to 80 points for power. 1 point per 100hp
        # Power is therefore capped at 8000hp by design, this isn't a hard limit, but raise a warning
        if self.power > 8000:
            utils.echo_message("Consist " + self.id + " has power > 8000hp, which is too much")
        power_cost_points = self.power / 100

        # Up to 20 points for speed up to 80mph. 1 point per 2mph
        speed_cost_points = min(self.speed, 80) / 2

        # Up to 80 points for speed above 80mph up to 200mph. 1 point per 1.5mph
        if self.speed > 200:
            utils.echo_message("Consist " + self.id + " has speed > 200, which is too much")
        high_speed_cost_points = max((self.speed - 80), 0) / 1.5

        # Up to 40 points for intro date after 1870. 1 point per 4 years.
        # Intro dates capped at 2030, this isn't a hard limit, but raise a warning
        if self.intro_date > 2030:
            utils.echo_message("Consist " + self.id + " has intro_date > 2030, which is too much")
        date_cost_points = max((self.intro_date - 1870), 0) / 4

        return power_cost_points + speed_cost_points + high_speed_cost_points + date_cost_points

    @property
    def buy_cost(self):
        # type_base_buy_cost_points is an arbitrary adjustment that can be applied on a type-by-type basis,
        return self.get_engine_cost_points() + self.type_base_buy_cost_points

    @property
    def running_cost(self):
        # type_base_running_cost_points is an arbitrary adjustment that can be applied on a type-by-type basis,
        return self.get_engine_cost_points() + self.type_base_running_cost_points


class WagonConsist(Consist):
    """
    Intermediate class for wagon consists to subclass from, provides some common properties.
    This class should be sparse - only declare the most limited set of properties common to wagon consists.
    """
    def __init__(self, type_config, speedy=False, **kwargs):
        id = self.get_wagon_id(type_config.base_id, **kwargs)
        kwargs['id'] = id
        kwargs['base_numeric_id'] = self.get_wagon_numeric_id(type_config.base_id, **kwargs)
        kwargs['track_type'] = type_config.track_type
        self.wagon_generation = kwargs.get('wagon_generation', None)
        super(WagonConsist, self).__init__(**kwargs)

        if self.track_type == 'NG':
            self.speed = global_constants.ng_wagon_speeds[speedy]
        else:
            if self.wagon_generation == 1:
                self.speed = global_constants.gen_1_wagon_speeds[speedy]
            elif self.wagon_generation == 2:
                self.speed = global_constants.gen_2_wagon_speeds[speedy]
            elif self.wagon_generation == 3:
                self.speed = global_constants.gen_3_wagon_speeds[speedy]

        self.num_cargo_rows = type_config.num_cargo_rows
        self.cargo_graphics_mappings = type_config.cargo_graphics_mappings
        self.generic_cargo_rows = type_config.generic_cargo_rows
        # register the consist so that buy menu order can later be built programatically
        vehicle_set = kwargs.get('vehicle_set')
        base_type = type_config.base_id
        vehicle_set_dict = registered_wagon_generations.setdefault(vehicle_set, {})
        base_type_list = vehicle_set_dict.setdefault(base_type, [])
        base_type_list.append(self.wagon_generation)
        base_type_list.sort()

    @property
    def buy_cost(self):
        if self.speed is not None:
            cost = self.speed
        else:
            cost = 125
        capacity_factors = []
        for slice in self.slices:
            if slice.default_cargo == 'PASS':
                # pax coaches have seats and stuff, are expensive to build
                capacity_factors.append(3 * getattr(slice, 'capacities_pax', 0)[1])
            elif slice.default_cargo == 'MAIL':
                # mail cars have pax-grade eqpt, but no seats etc, so moderately expensive
                capacity_factors.append(2 * getattr(slice, 'capacities_mail', 0)[1])
            else:
                capacity_factors.append(getattr(slice, 'capacities_freight', 0)[1])
        cost = cost + sum(capacity_factors)
        return 0.5 * cost # dibble all the things

    @property
    def running_cost(self):
        if self.speed is not None:
            cost = self.speed
        else:
            cost = 125
        if self.slices[0].default_cargo == 'PASS':
            return cost / 4
        elif self.slices[0].default_cargo == 'MAIL':
            return cost / 7
        else:
            return cost / 8

class Wagon(Train):
    """
    Intermediate class for actual cars (wagons) to subclass from, provides some common properties.
    This class should be sparse - only declare the most limited set of properties common to wagons.
    Most props should be declared by Train with useful defaults.
    """
    def __init__(self, type_config, **kwargs):
        super(Wagon, self).__init__(**kwargs)
        self.type_config = type_config
        self.template = type_config.template
        self.class_refit_groups = type_config.class_refit_groups
        self.label_refits_allowed = type_config.label_refits_allowed
        self.label_refits_disallowed = type_config.label_refits_disallowed
        self.autorefit = type_config.autorefit
        self.default_cargo = type_config.default_cargo
        self.default_cargo_capacities = self.get_capacity_variations(kwargs.get(type_config.default_capacity_type, 0))
        self.cargo_age_period = type_config.cargo_age_period


class SteamLoco(Train):
    """
    Steam Locomotive.
    """
    def __init__(self, **kwargs):
        super(SteamLoco, self).__init__(**kwargs)
        self.template = 'train.pynml'
        self.default_cargo_capacities = [0]
        self.engine_class = 'ENGINE_CLASS_STEAM'
        self.visual_effect = 'VISUAL_EFFECT_STEAM'
        # provide smoke near the front of a steam loco by default, can be over-ridden per vehicle
        self.visual_effect_offset = kwargs.get('visual_effect_offset', int(math.floor(-0.5 * self.vehicle_length)))


class SteamLocoTender(Train):
    """
    Steam Locomotive Tender.
    """
    def __init__(self, **kwargs):
        super(SteamLocoTender, self).__init__(**kwargs)
        self.template = 'train.pynml'
        self.default_cargo_capacities = [0]


class DieselLoco(Train):
    """
    Diesel Locomotive.
    """
    def __init__(self, **kwargs):
        super(DieselLoco, self).__init__(**kwargs)
        self.template = 'train.pynml'
        self.default_cargo_capacities = [0]
        self.engine_class = 'ENGINE_CLASS_DIESEL'
        self.visual_effect = 'VISUAL_EFFECT_DIESEL'


class DieselRailcar(Train):
    """
    Diesel Railcar (Single Unit).
    """
    def __init__(self, **kwargs):
        super(DieselRailcar, self).__init__(**kwargs)
        self.template = 'railcar.pynml'
        self.default_cargo_capacities = [0]
        self.class_refit_groups = ['pax', 'mail', 'express_freight']
        self.label_refits_allowed = [] # no specific labels needed
        self.label_refits_disallowed = []
        self.autorefit = True
        self.capacities_freight = [int(0.5 * capacity) for capacity in self.capacities_mail]
        self.default_cargo_capacities = self.capacities_pax
        self.default_cargo = 'PASS'
        self.engine_class = 'ENGINE_CLASS_DIESEL'
        self.visual_effect = 'VISUAL_EFFECT_DIESEL'


class ElectricLoco(Train):
    """
    Diesel Locomotive.
    """
    def __init__(self, **kwargs):
        super(ElectricLoco, self).__init__(**kwargs)
        self.template = 'train.pynml'
        self.default_cargo_capacities = [0]
        kwargs['consist'].track_type = "ELRL"
        self.engine_class = 'ENGINE_CLASS_ELECTRIC'
        self.visual_effect = 'VISUAL_EFFECT_ELECTRIC'


class ElectroDieselLoco(Train):
    """
    Bi-mode Locomotive - operates on electrical power or diesel.
    """
    def __init__(self, **kwargs):
        super(ElectroDieselLoco, self).__init__(**kwargs)
        self.template = 'train.pynml'
        self.default_cargo_capacities = [0]
        self.engine_class = 'ENGINE_CLASS_DIESEL'
        # visual effect handled in cb for this loco

class CargoSprinter(Train):
    """
    Freight Multiple Unit.
    """
    def __init__(self, **kwargs):
        super(CargoSprinter, self).__init__(**kwargs)
        self.template = 'cargo_sprinter.pynml'
        self.default_cargo_capacities = [0]
        self.class_refit_groups = ['express_freight']
        self.label_refits_allowed = [] # no specific labels needed
        self.label_refits_disallowed = []
        self.autorefit = True
        self.default_cargo_capacities = self.capacities_freight
        self.default_cargo = 'GOOD'
        self.engine_class = 'ENGINE_CLASS_DIESEL'
        self.visual_effect = 'VISUAL_EFFECT_DISABLE' # intended - positioning smoke correctly for this vehicle is too fiddly
        self.num_random_cargo_variants = kwargs.get('num_random_cargo_variants')
        self.loading_speed = 25


class MailCar(Wagon):
    """
    Mail Carriage.
    """
    def __init__(self, **kwargs):
        super(MailCar, self).__init__(**kwargs)
        self.capacities_freight = [int(0.5 * capacity) for capacity in self.capacities_mail]


class CombineCar(Wagon):
    """
    Carriage that offers capacity for both passengers (fixed) and mail / express cargo (refittable)
    """
    # this class is sparse - it exists to make special case handling easy by checking class type
    # combine car needs to set capacity_mail, capacity_freight, and capacity_pax
    # pax capacity is non-refittable and applied to lead slice of the unit
    def __init__(self, **kwargs):
        super(CombineCar, self).__init__(**kwargs)


class MetroMultipleUnit(Train):
    """
    Metro Unit
    """
    def __init__(self, **kwargs):
        super(MetroMultipleUnit, self).__init__(**kwargs)
        self.template = 'metro_mu.pynml'
        self.default_cargo_capacities = self.capacities_pax
        self.default_cargo = "PASS"
        self.engine_class = 'ENGINE_CLASS_ELECTRIC'
        self.visual_effect = 'VISUAL_EFFECT_ELECTRIC'
        self.loading_speed = 40


class MetroLoco(Train):
    """
    Metro Unit
    """
    def __init__(self, **kwargs):
        super(MetroLoco, self).__init__(**kwargs)
        self.template = 'train.pynml'
        self.default_cargo_capacities = [0]
        self.engine_class = 'ENGINE_CLASS_ELECTRIC'
        self.visual_effect = 'VISUAL_EFFECT_ELECTRIC'

