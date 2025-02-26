import math

# python builtin templater might be used in some utility cases
from string import Template

import polar_fox
import global_constants  # expose all constants for easy passing to templates
import spritelayer_cargos
import utils


class UnitBase(object):
    """
    Base class for all types of units
    """

    def __init__(self, **kwargs):
        # unit def is private, the public interface shouldn't use it, wrap @property methods around it as needed
        self._unit_def = kwargs["unit_def"]
        self.consist = kwargs.get("consist")
        # create an id, which is used for shared switch chains, and as base id for unit variants to construct an id
        if len(self.consist.unique_units) == 0:
            # first vehicle gets no numeric id suffix - for compatibility with buy menu list ids etc
            self.id = self.consist.id
            self.cabbage_numeric_id = 0
        else:
            self.id = self.consist.id + "_unit_" + str(len(self.consist.unique_units))
            self.cabbage_numeric_id = len(self.consist.unique_units)
        # create structure to hold the buyable variants, done last as may depend on other attrs of self
        # CABBAGE
        self.unit_variants = []
        # CABBAGE
        # !! the need to copy cargo refits from the consist is legacy from the default multi-unit articulated vehicles in Iron Horse 1
        # !! could likely be refactored !!
        self.label_refits_allowed = self.consist.label_refits_allowed
        self.label_refits_disallowed = self.consist.label_refits_disallowed
        self.autorefit = True
        # nml constant (STEAM is sane default)
        self.engine_class = "ENGINE_CLASS_STEAM"
        self.default_effect_z_offset = (
            12  # optimised for Pony diesel and electric trains
        )
        # 'symmetric' or 'asymmetric'?
        # defaults to symmetric, override in subclasses or per vehicle as needed
        self._symmetry_type = "symmetric"
        # optional - a switch name to trigger re-randomising vehicle random bits - override as need in subclasses
        self.random_trigger_switch = None

    @property
    def cabbage_unit_id_from_model_type(self):
        return self.consist.model_id + "_unit_" + str(self.cabbage_numeric_id)

    @property
    def tail_light(self):
        # optional - some engine units need to set explicit tail light spritesheets
        # subclasses may override this, e.g. wagons have an automatic tail light based on vehicle length
        if self._unit_def.tail_light is not None:
            return self._unit_def.tail_light
        else:
            return "empty"

    @property
    def effects(self):
        # empty by default, set in subtypes as needed
        return {}

    @property
    def rel_spriterow_index(self):
        if self._unit_def.rel_spriterow_index is not None:
            return self._unit_def.rel_spriterow_index
        else:
            return 0

    @property
    def capacity(self):
        if self._unit_def.capacity is not None:
            return self._unit_def.capacity
        else:
            return 0

    def get_capacity_variations(self, capacity):
        # capacity is variable, controlled by a newgrf parameter
        # allow that integer maths is needed for newgrf cb results; round up for safety
        try:
            result = [
                int(math.ceil(capacity * multiplier))
                for multiplier in global_constants.capacity_multipliers
            ]
        except:
            raise Exception(
                "get_capacity_variations" + " " + self.id + " " + self.consist.id
            )
        return result

    @property
    def capacities(self):
        return self.get_capacity_variations(self.capacity)

    @property
    def default_cargo_capacity(self):
        return self.capacities[2]

    @property
    def has_cargo_capacity(self):
        if self.default_cargo_capacity != 0:
            return True
        else:
            return False

    def get_pax_car_capacity(self):
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.pax_car_capacity_per_unit_length[
            self.consist.base_track_type_name
        ][self.consist.gen - 1]
        result = int(
            self.vehicle_length
            * base_capacity
            * self.consist.pax_car_capacity_type["multiplier"]
        )
        return result

    def get_mail_car_capacity(self):
        result = (
            int(self.get_freight_car_capacity()) / polar_fox.constants.mail_multiplier
        )
        return result

    def get_freight_car_capacity(self):
        # magic to set capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[
            self.consist.base_track_type_name
        ][self.consist.gen - 1]
        result = int(self.vehicle_length * base_capacity)
        return result

    @property
    def weight(self):
        # weight can be set explicitly via unit_def or by methods on subclasses
        return self._unit_def.weight

    @property
    def vehicle_length(self):
        # length of this unit, either derived from from chassis length, or set explicitly via keyword
        # first guard that one and only one of these props is set
        if (
            self._unit_def.vehicle_length is not None
            and self._unit_def.chassis is not None
        ):
            utils.echo_message(
                self.consist.id
                + " has units with both chassis and length properties set"
            )
        if self._unit_def.vehicle_length is None and self._unit_def.chassis is None:
            utils.echo_message(
                self.consist.id
                + " has units with neither chassis nor length properties set"
            )

        if self._unit_def.chassis is not None:
            # assume that chassis name format is 'foo_bar_ham_eggs_24px' or similar - true as of Nov 2020
            # if chassis name format changes / varies in future, just update the string slice accordingly, safe enough
            # splits on _, then takes last entry, then slices to remove 'px'
            result = int(self._unit_def.chassis.split("_")[-1][0:-2])
            return int(result / 4)
        else:
            return self._unit_def.vehicle_length

    @property
    def availability(self):
        # only show vehicle in buy menu if it is first vehicle in consist
        if self.is_lead_unit_of_consist:
            return "ALL_CLIMATES"
        else:
            return "NO_CLIMATE"

    @property
    def is_lead_unit_of_consist(self):
        if self.consist.units.index(self) == 0:
            return True
        else:
            return False

    @property
    def symmetry_type(self):
        if self._unit_def.symmetry_type is not None:
            symmetry_type = self._unit_def.symmetry_type
        else:
            symmetry_type = self._symmetry_type
        assert symmetry_type in [
            "symmetric",
            "asymmetric",
        ], "symmetry_type '%s' is invalid in %s" % (
            symmetry_type,
            self.consist.id,
        )
        return symmetry_type

    @property
    def misc_flags(self):
        # note that there are both misc_flags and extra_flags, for grf_spec reasons
        misc_flags = ["TRAIN_FLAG_2CC", "TRAIN_FLAG_SPRITE_STACK"]
        if self.autorefit:
            misc_flags.append("TRAIN_FLAG_AUTOREFIT")
        if self.consist.tilt_bonus:
            misc_flags.append("TRAIN_FLAG_TILT")
        if self.consist.train_flag_mu:
            misc_flags.append("TRAIN_FLAG_MU")
        return ",".join(misc_flags)

    def get_extra_flags(self, unit_variant):
        extra_flags = []
        if unit_variant.buyable_variant.buyable_variant_group is not None:
            # some of these aren't needed for wagons or articulated trailing parts, but eh, probably fine?
            # disable news and exclusive preview for all variants except the default
            if (
                unit_variant.buyable_variant.get_variant_group_parent_vehicle_id()
                is not None
            ):
                extra_flags.append("VEHICLE_FLAG_DISABLE_NEW_VEHICLE_MESSAGE")
                extra_flags.append("VEHICLE_FLAG_DISABLE_EXCLUSIVE_PREVIEW")
            extra_flags.append("VEHICLE_FLAG_SYNC_VARIANT_EXCLUSIVE_PREVIEW")
            extra_flags.append("VEHICLE_FLAG_SYNC_VARIANT_RELIABILITY")
        return ",".join(extra_flags)

    def get_cargo_classes_for_nml(self, allow_disallow_key):
        result = []
        # maps lists of allowed classes.  No equivalent for disallowed classes, that's overly restrictive and damages the viability of class-based refitting
        if hasattr(self, "articulated_unit_different_class_refit_groups"):
            # in *rare* cases an articulated unit might need different refit classes to its parent consist
            class_refit_groups = self.articulated_unit_different_class_refit_groups
        else:
            # by default get the refit classes from the consist
            class_refit_groups = self.consist.class_refit_groups
        for class_refit_group in class_refit_groups:
            for cargo_class in global_constants.base_refits_by_class[class_refit_group][
                allow_disallow_key
            ]:
                result.append(cargo_class)
        # !! this does not currently support train prop 0x32 (filter allowed classes)
        # !! if that's needed, then branch on allow_disallow_key == "allowed":
        return "bitmask(" + ",".join(result) + ")"

    @property
    def loading_speed(self):
        # ottd vehicles load at different rates depending on type, train default is 5
        # Iron Horse uses 5 as default, with some vehicle types adjusting that up or down
        return int(5 * self.consist.loading_speed_multiplier)

    @property
    def running_cost_base(self):
        # all engines use the same RUNNING_COST_STEAM, and Iron Horse provides the variation between steam/electric/diesel
        # this will break base cost mod grfs, but "Pikka says it's ok"
        # wagons will use RUNNING_COST_DIESEL - set in wagon subclass
        return "RUNNING_COST_STEAM"

    @property
    def roof(self):
        # fetch spritesheet name to use for roof when generating graphics
        if self.consist.roof_type is not None:
            if self.consist.base_track_type_name == "NG":
                ng_prefix = "ng_"
            else:
                ng_prefix = ""
            return (
                str(4 * self.vehicle_length)
                + "px_"
                + ng_prefix
                + self.consist.roof_type
            )
        else:
            return None

    @property
    def requires_colour_mapping_cb(self):
        # bit weird and janky, various conditions to consider eh
        if getattr(self.consist, "use_colour_randomisation_strategies", False):
            return "use_colour_randomisation_strategies"
        elif (
            getattr(self.consist.gestalt_graphics, "colour_mapping_switch", None)
            is not None
        ):
            if self.consist.gestalt_graphics.colour_mapping_with_purchase:
                return "colour_mapping_switch_with_purchase"
        else:
            return None

    @property
    def effects_vary_by_power_source(self):
        # simple check if more than one type of effect is defined
        return len(self.effects) > 1

    @property
    def default_effect_offsets(self):
        # override this in subclasses as needed (e.g. to move steam engine smoke to front by default
        # vehicles can also override this via _unit_def
        return [(0, 0)]

    def get_nml_expression_for_effects(self, railtype="default"):
        # provides part of nml switch for effects (smoke)

        # effects can be over-ridden per vehicle, or use a default from the vehicle subclass
        if self._unit_def.effect_offsets is not None:
            effect_offsets = self._unit_def.effect_offsets
        else:
            effect_offsets = self.default_effect_offsets

        if self.consist.id == "toaster":
            print("TOASTER", effect_offsets)

        # z offset is handled independently to x, y for simplicity, option to override z offset default per vehicle
        if self._unit_def.effect_z_offset is not None:
            z_offset = self._unit_def.effect_z_offset
        else:
            z_offset = self.default_effect_z_offset

        # changing sprite by railtype is supported, changing position is *not* as of August 2019
        effect_sprite = self.effects[railtype][1]

        result = []
        for index, offset_pair in enumerate(effect_offsets):
            items = [
                effect_sprite,
                str(offset_pair[0]),
                str(offset_pair[1]),
                str(z_offset),
            ]
            result.append(
                "STORE_TEMP(create_effect("
                + ",".join(items)
                + "), 0x10"
                + str(index)
                + ")"
            )
        return [
            "[" + ",".join(result) + "]",
            str(len(result)) + " + CB_RESULT_CREATE_EFFECT_CENTER",
        ]

    def get_nml_expression_for_grfid_of_neighbouring_unit(self, unit_offset):
        expression_template = Template(
            "[STORE_TEMP(${unit_offset}, 0x10F), var[0x61, 0, 0xFFFFFFFF, 0x25]]"
        )
        return expression_template.substitute(unit_offset=unit_offset)

    def get_nml_expression_for_id_of_neighbouring_unit(self, unit_offset):
        # best used with the check for same grfid, but eh
        expression_template = Template(
            "[STORE_TEMP(${unit_offset}, 0x10F), var[0x61, 0, 0x0000FFFF, 0xC6]]"
        )
        return expression_template.substitute(unit_offset=unit_offset)

    def get_spriteset_template_name(self, reversed, y):
        template_name = "_".join(
            [
                "spriteset_template",
                self.symmetry_type,
                reversed,
                str(self.vehicle_length),
                "8",
            ]
        )
        anim_flag = (
            "ANIM" if self.consist.suppress_animated_pixel_warnings else "NOANIM"
        )
        args = ",".join([str(y), anim_flag])
        return template_name + "(" + args + ")"

    def get_label_refits_allowed(self):
        # allowed labels, for fine-grained control in addition to classes
        return ",".join(self.label_refits_allowed)

    def get_label_refits_disallowed(self):
        # disallowed labels, for fine-grained control, knocking out cargos that are allowed by classes, but don't fit for gameplay reasons
        return ",".join(self.label_refits_disallowed)

    def get_cargo_suffix(self):
        return "string(" + self.cargo_units_refit_menu + ")"

    def assert_random_reverse(self):
        # some templates don't support the random_reverse (by design, they're symmetrical sprites, and reversing bloats the template)
        if self.consist.random_reverse:
            if hasattr(self.consist, "gestalt_graphics"):
                for nml_template in [
                    "vehicle_box_car_with_opening_doors.pynml",
                    "vehicle_with_cargo_specific_liveries.pynml",
                    "vehicle_consist_position_dependent.pynml",
                ]:
                    assert self.consist.gestalt_graphics.nml_template != nml_template, (
                        "%s has 'random_reverse set True, which isn't supported by nml_template %s"
                        % (self.consist.id, nml_template)
                    )

    def assert_cargo_labels(self, cargo_labels):
        for i in cargo_labels:
            if i not in global_constants.cargo_labels:
                utils.echo_message(
                    "Warning: vehicle "
                    + self.id
                    + " references cargo label "
                    + i
                    + " which is not defined in the cargo table"
                )

    def render(self, templates, graphics_path):
        # integrity tests
        self.assert_cargo_labels(self.label_refits_allowed)
        self.assert_cargo_labels(self.label_refits_disallowed)
        self.assert_random_reverse()
        # test interpolated gen and intro_year
        assert self.consist.gen, (
            "%s consist.gen is None, which is invalid.  Set gen or intro_year" % self.id
        )
        assert self.consist.intro_year, (
            "%s consist.gen is None, which is invalid.  Set gen or intro_year" % self.id
        )
        # templating
        template_name = self.consist.gestalt_graphics.nml_template
        template = templates[template_name]
        nml_result = template(
            vehicle=self,
            consist=self.consist,
            cabbage_catalogue_entry=self.consist.cabbage_catalogue_entry,
            factory=self.consist.factory,
            global_constants=global_constants,
            utils=utils,
            temp_storage_ids=global_constants.temp_storage_ids,  # convenience measure
            graphics_path=graphics_path,
            spritelayer_cargos=spritelayer_cargos,
        )
        return nml_result


class BatteryHybridEngineUnit(UnitBase):
    """
    Unit for a battery hybrid engine.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"
        # most battery hybrid engines are asymmetric, override per vehicle as needed
        self._symmetry_type = kwargs.get("symmetry_type", "asymmetric")

    @property
    def effects(self):
        return {"default": ["EFFECT_SPAWN_MODEL_DIESEL", "EFFECT_SPRITE_STEAM"]}


class CabbageDVTUnit(UnitBase):
    """
    Unit for a DVT / Cabbage (driving cab with mail capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"  # probably fine?
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        return {}

    @property
    def capacity(self):
        return self.get_mail_car_capacity()


class CabControlPaxCarUnit(UnitBase):
    """
    Unit for a cab control car (driving cab with pax capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"  # probably fine?
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        return {}

    @property
    def capacity(self):
        return self.get_pax_car_capacity()


class CombineUnitMailBase(UnitBase):
    """
    Mail unit for a combine vehicle (articulated consist with mail + pax capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # usually refit classes come from consist, but we special case to the unit for this combine coach
        self.articulated_unit_different_class_refit_groups = [
            "mail"
        ]  # note mail only, no other express cargos

    @property
    def capacity(self):
        # 0.75 is to account for some pax capacity 'on' this unit (implemented on adjacent pax unit)
        return 0.75 * self.get_mail_car_capacity()


class CombineUnitPaxBase(UnitBase):
    """
    Pax unit for a combine vehicle (articulated consist with mail + pax capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # usually refit classes come from consist, but we special case to the unit for this combine coach
        self.articulated_unit_different_class_refit_groups = ["pax"]

    @property
    def capacity(self):
        return self.get_pax_car_capacity()


class AutoCoachCombineUnitMail(CombineUnitMailBase):
    """
    Mail unit for a combine auto coach (articulated driving cab consist with mail + pax capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_STEAM"
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        return {}


class AutoCoachCombineUnitPax(CombineUnitPaxBase):
    """
    Pax unit for a combine auto coach (articulated driving cab consist with mail + pax capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_STEAM"
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        return {}


class DieselRailcarCombineUnitMail(CombineUnitMailBase):
    """
    Mail unit for a combine diesel railcar (articulated consist with mail + pax capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        return {"default": ["EFFECT_SPAWN_MODEL_DIESEL", "EFFECT_SPRITE_DIESEL"]}


class DieselRailcarCombineUnitPax(CombineUnitPaxBase):
    """
    Pax unit for a combine diesel railcar (articulated consist with mail + pax capacity)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        return {"default": ["EFFECT_SPAWN_MODEL_DIESEL", "EFFECT_SPRITE_DIESEL"]}


class DieselEngineUnit(UnitBase):
    """
    Unit for a diesel engine.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"
        # most diesel engines are asymmetric, override per vehicle as needed
        self._symmetry_type = kwargs.get("symmetry_type", "asymmetric")

    @property
    def effects(self):
        return {"default": ["EFFECT_SPAWN_MODEL_DIESEL", "EFFECT_SPRITE_DIESEL"]}


class DieselRailcarBaseUnit(DieselEngineUnit):
    """
    Unit for a diesel railcar.  Just a sparse subclass to set symmetry.  Capacity set in subclasses
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # the cab magic won't work unless it's asymmetric eh? :)
        self._symmetry_type = kwargs.get("symmetry_type", "asymmetric")
        # note that railcar effects are left in default position, no attempt to move them to end of vehicle, or double them (tried, looks weird)


class DieselExpressRailcarPaxUnit(DieselRailcarBaseUnit):
    """
    Unit for a pax diesel express railcar.  Just a sparse subclass to set capacity and effects.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # effects
        self.engine_class = "ENGINE_CLASS_DIESEL"

    @property
    def effects(self):
        return {"default": ["EFFECT_SPAWN_MODEL_DIESEL", "EFFECT_SPRITE_DIESEL"]}

    @property
    def capacity(self):
        return self.get_pax_car_capacity()


class DieselRailcarMailUnit(DieselRailcarBaseUnit):
    """
    Unit for a mail diesel railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def capacity(self):
        return self.get_mail_car_capacity()


class DieselRailcarPaxUnit(DieselRailcarBaseUnit):
    """
    Unit for a pax diesel railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def capacity(self):
        return self.get_pax_car_capacity()


class ElectricEngineUnit(UnitBase):
    """
    Unit for an electric engine.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_ELECTRIC"
        # almost all electric engines are asymmetric, override per vehicle as needed
        self._symmetry_type = kwargs.get("symmetry_type", "asymmetric")

    @property
    def effects(self):
        # option to suppress default effects here via unit_def
        if self._unit_def.effects is not None:
            return self._unit_def.effects
        else:
            return {
                "default": ["EFFECT_SPAWN_MODEL_ELECTRIC", "EFFECT_SPRITE_ELECTRIC"]
            }


class ElectricHighSpeedUnitBase(UnitBase):
    """
    Unit for high-speed, high-power electric train
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_ELECTRIC"
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        # option to suppress default effects here via unit_def
        if self._unit_def.effects is not None:
            return self._unit_def.effects
        else:
            return {
                "default": ["EFFECT_SPAWN_MODEL_ELECTRIC", "EFFECT_SPRITE_ELECTRIC"]
            }


class ElectricHighSpeedMailUnit(ElectricHighSpeedUnitBase):
    """
    Mail unit for high-speed, high-power electric train
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def capacity(self):
        return self.get_mail_car_capacity()


class ElectricHighSpeedPaxUnit(ElectricHighSpeedUnitBase):
    """
    Passenger unit for high-speed, high-power electric train
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def capacity(self):
        # this won't work with double deck high speed in future, extend a class for that then if needed
        return self.get_pax_car_capacity()


class ElectroDieselEngineUnit(UnitBase):
    """
    Unit for a bi-mode Locomotive - operates on electrical power or diesel.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"
        # electro-diesels are complex eh?
        self.consist.electro_diesel_buy_cost_malus = 1  # will get same buy cost factor as electric engine of same gen (blah balancing)
        # almost all electro-diesel engines are asymmetric, override per vehicle as needed
        self._symmetry_type = kwargs.get("symmetry_type", "asymmetric")

    @property
    def effects(self):
        return {
            "default": ["EFFECT_SPAWN_MODEL_DIESEL", "EFFECT_SPRITE_DIESEL"],
            "electrified": ["EFFECT_SPAWN_MODEL_ELECTRIC", "EFFECT_SPRITE_ELECTRIC"],
        }


class ElectroDieselRailcarBaseUnit(UnitBase):
    """
    Unit for a bi-mode railcar - operates on electrical power or diesel.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"
        # electro-diesels are complex eh?
        self.consist.electro_diesel_buy_cost_malus = 1.15  # will get higher buy cost factor than electric railcar of same gen (blah balancing)
        # the cab magic won't work unless it's asymmetrical eh? :P
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        return {
            "default": ["EFFECT_SPAWN_MODEL_DIESEL", "EFFECT_SPRITE_DIESEL"],
            "electrified": ["EFFECT_SPAWN_MODEL_ELECTRIC", "EFFECT_SPRITE_ELECTRIC"],
        }


class ElectroDieselRailcarMailUnit(ElectroDieselRailcarBaseUnit):
    """
    Unit for a mail electro-diesel railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def capacity(self):
        return self.get_mail_car_capacity()


class ElectroDieselExpressRailcarPaxUnit(ElectroDieselRailcarBaseUnit):
    """
    Unit for a pax electro-diesel express railcar.  Just a sparse subclass to set and effects.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # effects
        self.engine_class = "ENGINE_CLASS_DIESEL"

    @property
    def effects(self):
        return {
            "default": ["EFFECT_SPAWN_MODEL_DIESEL", "EFFECT_SPRITE_DIESEL"],
            "electrified": ["EFFECT_SPAWN_MODEL_ELECTRIC", "EFFECT_SPRITE_ELECTRIC"],
        }

    @property
    def capacity(self):
        return self.get_pax_car_capacity()


class ElectricRailcarBaseUnit(UnitBase):
    """
    Unit for an electric railcar.  Capacity set in subclasses
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_ELECTRIC"
        # the cab magic won't work unless it's asymmetrical eh? :P
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        return {"default": ["EFFECT_SPAWN_MODEL_ELECTRIC", "EFFECT_SPRITE_ELECTRIC"]}


class ElectricExpressRailcarPaxUnit(ElectricRailcarBaseUnit):
    """
    Unit for a express pax electric railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def capacity(self):
        return self.get_pax_car_capacity()


class ElectricRailcarMailUnit(ElectricRailcarBaseUnit):
    """
    Unit for a mail electric railcar.  Just a sparse subclass to set capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def capacity(self):
        return self.get_mail_car_capacity()


class ElectricRailcarPaxUnit(ElectricRailcarBaseUnit):
    """
    Unit for a pax electric railcar.  Just a sparse subclass to set capacity and force the second livery to be used via dubious means.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def capacity(self):
        return self.get_pax_car_capacity()


class MetroUnit(UnitBase):
    """
    Unit for an electric metro train, with high loading speed.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_ELECTRIC"
        self.default_effect_z_offset = (
            1  # optimised for Pony diesel and electric trains
        )
        # the cab magic won't work unless it's asymmetrical eh? :P
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        return {"default": ["EFFECT_SPAWN_MODEL_ELECTRIC", "EFFECT_SPRITE_ELECTRIC"]}

    @property
    def capacity(self):
        if self._unit_def.capacity is not None:
            return self._unit_def.capacity
        else:
            return 0


class SnowploughUnit(UnitBase):
    """
    Unit for a snowplough.  Snowploughs have express cargo capacity, so they can actually be useful. :P
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_DIESEL"  # !! needs changing??
        self._symmetry_type = "asymmetric"

    @property
    def effects(self):
        return {}

    @property
    def capacity(self):
        return self.get_mail_car_capacity()


class SteamEnginePoweredUnit(UnitBase):
    """
    Unit for a steam engine, with smoke
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine_class = "ENGINE_CLASS_STEAM"
        self.default_effect_z_offset = 13  # optimised for Pony steam trains
        self._symmetry_type = "asymmetric"  # assume all steam engines are asymmetric

    @property
    def effects(self):
        return {"default": ["EFFECT_SPAWN_MODEL_STEAM", "EFFECT_SPRITE_STEAM"]}

    @property
    def default_effect_offsets(self):
        # force steam engine smoke to front by default, can also override per unit for more precise positioning
        return [(1 + int(math.floor(-0.5 * self.vehicle_length)), 0)]


class SteamEngineTenderUnit(UnitBase):
    """
    Unit for a steam engine tender.
    Arguably this class is pointless, as it is just passthrough.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # assume all steam engine tenders are asymmetric
        self._symmetry_type = "asymmetric"


# alphabetised (mostly) non-CarUnitBase subclasses of UnitBase above here
# then CarUnitBase subclasses below here, also alphabetised


class CarUnitBase(UnitBase):
    """
    Intermediate class for actual cars (wagons) to subclass from, provides some common properties.
    This class should be sparse - only declare the most limited set of properties common to wagons.
    Most props should be declared by UnitBase with useful defaults.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.consist = kwargs["consist"]
        # most wagons are symmetric, override per vehicle or subclass as needed
        self._symmetry_type = kwargs.get("symmetry_type", "symmetric")

    @property
    def tail_light(self):
        # all wagons use auto tail-lights based on length
        # override in subclass if needed
        return str(self.vehicle_length * 4) + "px"

    @property
    def running_cost_base(self):
        # all wagons use the same RUNNING_COST_DIESEL, this is nerfed down to give appropriate increments for low wagon run costs
        # this will break base cost mod grfs, but "Pikka says it's ok"
        # engines will all use RUNNING_COST_STEAM
        return "RUNNING_COST_DIESEL"

    @property
    def weight(self):
        # set weight based on capacity  * a multiplier from consist * roster gen factor
        return int(
            self.consist.weight_factor
            * self.default_cargo_capacity
            * self.consist.roster.train_car_weight_factors[self.consist.gen - 1]
        )


class AlignmentCarUnit(CarUnitBase):
    """
    Alignment Car, for debugging sprite positions
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._symmetry_type = "asymmetric"


class CabooseCarUnit(CarUnitBase):
    """
    Caboose Car. This subclass only exists to set weight in absence of cargo capacity, in other respects it's just a standard wagon.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # caboose cars may be asymmetric, they are also user-flippable as of August 2022
        self._symmetry_type = "asymmetric"

    @property
    def weight(self):
        # special handling of weight
        weight_factor = 3 if self.consist.base_track_type_name == "NG" else 5
        return weight_factor * self.vehicle_length

    @property
    def capacity(self):
        return 0


class PaxCarUnit(CarUnitBase):
    """
    Pax wagon. This subclass only exists to set capacity and symmetry_type.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # pax wagons may be asymmetric, there is magic in the graphics processing to make this work
        self._symmetry_type = "asymmetric"

    @property
    def capacity(self):
        return self.get_pax_car_capacity()


class PaxRailcarTrailerCarUnit(PaxCarUnit):
    """
    Railcar (or railbus) unpowered pax trailer. This subclass only exists to set tail light
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def tail_light(self):
        # CarUnitBase sets auto tail light, override it in unit_def, fail if not set
        assert (
            self._unit_def.tail_light is not None
        ), "%s consist has a unit without tail_light set, which is required for %s" % (
            self.id,
            self.__class__.__name__,
        )
        return self._unit_def.tail_light


class PaxRestaurantCarUnit(PaxCarUnit):
    """
    Restaurant (special) pax wagon. This subclass only exists to set special weight handling
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def weight(self):
        # special handling of weight - let's just use 37 + gen for Pony, split that later for other rosters if needed
        return 37 + self.consist.gen


class ExpressCarUnit(CarUnitBase):
    """
    Express freight car.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def capacity(self):
        return self.get_mail_car_capacity()


class ExpressIntermodalCarUnit(ExpressCarUnit):
    """
    Express container car, subclassed from express car.  This subclass only exists to symmetry_type and random trigger.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # express intermodal cars may be asymmetric, there is magic in the graphics processing to make this work
        self._symmetry_type = "asymmetric"
        self.random_trigger_switch = (
            "_switch_graphics_spritelayer_cargos_"
            + self.consist.spritelayer_cargo_layers[0]
        )


class ExpressMailCarUnit(ExpressCarUnit):
    """
    Mail wagon, subclassed from express car.  Only exists to set symmetry_type.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # mail wagons may be asymmetric, there is magic in the graphics processing to make symmetric pax/mail sprites also work with this
        self._symmetry_type = "asymmetric"


class MailRailcarTrailerCarUnit(ExpressCarUnit):
    """
    Railcar (or railbus) unpowered mail trailer. This subclass only exists to set tail light and symmetry type.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._symmetry_type = "asymmetric"

    @property
    def tail_light(self):
        # CarUnitBase sets auto tail light, override it in unit_def, fail if not set
        assert (
            self._unit_def.tail_light is not None
        ), "%s consist has a unit without tail_light set, which is required for %s" % (
            self.id,
            self.__class__.__name__,
        )
        return self._unit_def.tail_light


class AutomobileCarAsymmetricUnit(ExpressCarUnit):
    """
    Automobile (cars, trucks, tractors) transporter car, subclassed from express car.
    This subclass exists to set symmetry_type and random trigger.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # some vehicle transporter cars are asymmetric
        self._symmetry_type = "asymmetric"
        utils.echo_message(
            "AutomobileCarAsymmetricUnit random_trigger_switch is using _switch_graphics_spritelayer_cargos "
            + self.consist.id
        )
        self.random_trigger_switch = (
            "_switch_graphics_spritelayer_cargos_"
            + self.consist.spritelayer_cargo_layers[0]
        )


class AutomobileCarSymmetricUnit(ExpressCarUnit):
    """
    Automobile (cars, trucks, tractors) transporter car, subclassed from express car.
    This subclass exists to set symmetry_type and random trigger.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # some vehicle transporter cars are symmetric
        self._symmetry_type = "symmetric"
        utils.echo_message(
            "AutomobileCarSymmetricUnit random_trigger_switch is using _switch_graphics_spritelayer_cargos "
            + self.consist.id
        )
        self.random_trigger_switch = (
            "_switch_graphics_spritelayer_cargos_"
            + self.consist.spritelayer_cargo_layers[0]
        )


class FreightCarUnit(CarUnitBase):
    """
    Freight wagon.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def capacity(self):
        if self._unit_def.capacity is not None:
            print(
                self.consist.id,
                self.id,
                " has a capacity set in init - possibly incorrect",
                self._unit_def.capacity,
            )
        # magic to set freight car capacity subject to length
        base_capacity = self.consist.roster.freight_car_capacity_per_unit_length[
            self.consist.base_track_type_name
        ][self.consist.gen - 1]
        return self.vehicle_length * base_capacity


class BinCarUnit(FreightCarUnit):
    """
    Peat wagon, cane bin car. This subclass only exists to set the capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def capacity(self):
        # just double whatever is set by the init, what could go wrong? :)
        return 2 * self.get_freight_car_capacity()


class CoilBuggyCarUnit(FreightCarUnit):
    """
    Coil buggy car. This subclass only exists to set the capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def capacity(self):
        # just double whatever is set by the init, what could go wrong? :)
        return 2 * self.get_freight_car_capacity()


class CoilCarAsymmetricUnit(FreightCarUnit):
    """
    Asymmetric coil car. This subclass sets the symmetry_type to asymmetric.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._symmetry_type = "asymmetric"


class HeavyDutyCarUnit(FreightCarUnit):
    """
    Heavy duty car. This subclass only exists to set the capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def capacity(self):
        # just double whatever is set by the init, what could go wrong? :)
        return 2 * self.get_freight_car_capacity()


class IngotCarUnit(FreightCarUnit):
    """
    Ingot car. This subclass only exists to set the capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def capacity(self):
        # just double whatever is set by the init, what could go wrong? :)
        return 2 * self.get_freight_car_capacity()


class IntermodalCarUnit(FreightCarUnit):
    """
    Intermodal Car. This subclass only exists to symmetry_type, random trigger and colour mapping switches.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # intermodal cars may be asymmetric, there is magic in the graphics processing to make this work
        self._symmetry_type = "asymmetric"
        self.random_trigger_switch = (
            "_switch_graphics_spritelayer_cargos_"
            + self.consist.spritelayer_cargo_layers[0]
        )


class OreDumpCarUnit(FreightCarUnit):
    """
    Ore dump car. This subclass sets the symmetry_type to asymmetric.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._symmetry_type = "asymmetric"


class SlagLadleCarUnit(FreightCarUnit):
    """
    Slag ladle car. This subclass only exists to set the capacity.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def capacity(self):
        # just double whatever is set by the init, what could go wrong? :)
        return 2 * self.get_freight_car_capacity()


class TorpedoCarUnit(FreightCarUnit):
    """
    Torpedo car. This subclass sets the symmetry_type to asymmetric.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._symmetry_type = "asymmetric"

    @property
    def capacity(self):
        # capacity bonus is solely to support using small stations in Steeltown where space between industries is constrained
        # just multiply whatever is set by the init, what could go wrong? :)
        return 1.5 * self.get_freight_car_capacity()
