from functools import cached_property

import polar_fox
import gestalt_graphics.graphics_constants as graphics_constants
from gestalt_graphics import pipelines
import utils
from utils import timing

# get args passed by makefile
command_line_args = utils.get_command_line_args()

# possibly move to graphics constants?
formation_ruleset_reporting_label_maps = {
    "max_1_unit_sets": {"label": "model_id", "delegate_to_catalogue": True},
    "max_2_unit_sets": {"label": "model_id", "delegate_to_catalogue": True},
    "max_4_unit_sets": {"label": "model_id", "delegate_to_catalogue": True},
    "motorail_cars": {"label": "motorail_car"},
    "driving_cab_cars": {"label": "generic_pax_car"},
    "metro": {"label": "vehicle_family", "delegate_to_catalogue": True},
    "mail_cars": {"label": "generic_mail_car"},
    "pax_cars": {"label": "generic_pax_car"},
    "restaurant_cars": {"label": "generic_pax_car"},
    "railcars_2_unit_sets": {"label": "vehicle_family", "delegate_to_catalogue": True},
    "railcars_3_unit_sets": {"label": "vehicle_family", "delegate_to_catalogue": True},
    "railcars_4_unit_sets": {"label": "vehicle_family", "delegate_to_catalogue": True},
    "railcars_6_unit_sets": {"label": "vehicle_family", "delegate_to_catalogue": True},
    "tgv_hst": {"label": "tgv_hst", "delegate_to_catalogue": True},
}


class GestaltGraphics(object):
    """
    Simple class, which is extended in subclasses to configure:
     - base vehicle recolour (if any)
     - cargo graphics (if any)
     - pantographs (if any)
     - other processing as required
    """

    def __init__(self, **kwargs):
        self.catalogue_entry = kwargs["catalogue_entry"]
        # by default, pipelines are empty
        self.pipelines = pipelines.get_pipelines([])
        # sometimes processing may depend on another generated vehicle spritesheet, so there are multiple processing priorities, 1 = highest
        self.render_pass_num = 1
        # default value for optional mask layer, this is JFDI for 2022, may need converting a more generic spritelayers structure in future
        # set directly by the model variant self.gestalt_graphics.add_masked_overlay = True, or by kwargs on a specific gestalt subclass
        self.add_masked_overlay = False
        self.buy_menu_width_addition = 0
        # override this in subclasses as needed
        self.num_load_state_or_similar_spriterows = 1
        # optional - rulesets are used to define for different types of vehicle how sprites change depending on formation position
        # ruleset may also be used for buy menu sprite processing
        self.formation_ruleset = kwargs.get("formation_ruleset", None)
        # !! we need a way to get a useful (if not perfect) debug vehicle image for checking pantograph positions, and this lets us force useful rows for vehicle and pan
        self.jfdi_pantograph_debug_image_y_offsets = kwargs.get(
            "jfdi_pantograph_debug_image_y_offsets", [0, 0]
        )

    @cached_property
    def catalogue(self):
        # convenience function - but catalogue_entry might be none in some contexts
        if self.catalogue_entry is not None:
            return self.catalogue_entry.catalogue
        else:
            return None

    @property
    def nml_template(self):
        # override in subclasses as needed
        # return a pnml file name, e.g. `return 'vehicle_default.pynml'`
        return None

    @property
    def variants_use_common_graphics_switch_chain(self):
        return False

    def get_output_row_types(self):
        # stub, for compatibility reasons
        return ["single_row"]

    def buy_menu_row_map(self, pipeline):
        # return a structure for buy_menu_row_map conforming to:
        # [
        #   {
        #       "spriterow_num_dest": int for destination spriterow num in output spritesheet,
        #       "source_vehicles_and_input_spriterow_nums": [(vehicle unit class instance, int for input spriterow in input spritesheet), (...)],
        #   },
        #   {...},
        # ]
        # the gestalt should internally take care of anything like position-dependent sprites and return an appropriate row_map
        # that covers the majority of cases
        # if any special cases are needed (e.g. randomised wagon sprites) do one of the following:
        # option 1. subclass this function in the gestalt
        # option 2. a gestalt subclass can be configured to use an alternative pipeline for the buy menu sprite

        result = []
        if pipeline.is_pantographs_pipeline:
            # pans are the same for all buyable variants, and are just provided either once, or per formation position
            dest_spriterows = [pipeline.catalogue.default_entry]
        else:
            # dest_spriterows is equivalent to liveries in catalogue
            dest_spriterows = pipeline.catalogue
        for dest_spriterow_counter, catalogue_entry in enumerate(dest_spriterows):
            source_vehicles_and_input_spriterow_nums = []

            for unit_counter, unit in enumerate(pipeline.example_model_variant.units):
                # vehicle unit, y offset (num spriterows) to buy menu input row
                source_vehicles_and_input_spriterow_nums.append(
                    [
                        unit,
                        self.get_buy_menu_unit_input_row_num(
                            pipeline, catalogue_entry, unit_counter, unit
                        ),
                    ]
                )

            # the spritesheet has buy menu sprites in their own descending vertical order corresponding to buyable variants
            # the custom buy menu sprites don't align vertically with any specific vehicle spriterow and have dedicated nml templating
            row_config = {
                "spriterow_num_dest": dest_spriterow_counter,
                "source_vehicles_and_input_spriterow_nums": source_vehicles_and_input_spriterow_nums,
            }
            result.append(row_config)
        return result

    def get_buy_menu_unit_input_row_num(
        self, pipeline, catalogue_entry, unit_counter, unit
    ):
        # override in subclasses as needed
        result = (unit.rel_spriterow_index * len(pipeline.catalogue)) + (
            catalogue_entry.livery_def.relative_spriterow_num
            * self.num_load_state_or_similar_spriterows
        )
        return result

    @property
    def badge_slug_for_alt_var_41_predicate(self):
        # we use a badge as a predicate to detect 'same formation' for rulesets
        # this gets a slug for assembling the badge
        # we go via gestalt_graphics as that's the proper domain for rulesets...
        # ...catalogue should not know about rulesets
        # however gestalt_graphics equally doesn't know about specific model types...
        # ...so it delegates back to catalogue methods or properties
        # the result is a bit conditional / indirect, but the domain boundaries are faffy here
        if self.formation_ruleset is None:
            return None
        reporting_label_map = formation_ruleset_reporting_label_maps[
            self.formation_ruleset
        ]
        if reporting_label_map.get("delegate_to_catalogue", False):
            if reporting_label_map["label"] == "model_id":
                return self.catalogue.model_id
            if reporting_label_map["label"] == "vehicle_family":
                return self.catalogue.vehicle_family_id
            if reporting_label_map["label"] == "tgv_hst":
                return (
                    self.catalogue.tgv_hst_quacker.formation_ruleset_middle_part_equivalence_flag
                )
        return reporting_label_map["label"]


class GestaltGraphicsEngine(GestaltGraphics):
    """
    Simple Gestalt specifically for engines that have absolutely no other graphics processing except pantograph generation.
    Any Gestalt can also add pantographs as needed (it's a method on Pipeline base class).
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pipelines = pipelines.get_pipelines(
            ["pass_through_pipeline", "generate_buy_menu_sprite_vanilla_vehicle"]
        )
        self.colour_mapping_switch = "_switch_colour_mapping"
        self.colour_mapping_switch_purchase = "_switch_colour_mapping"
        self.colour_mapping_with_purchase = True
        # add pantographs as necessary
        if kwargs.get("pantograph_type", None) is not None:
            self.pipelines.extend(
                pipelines.get_pipelines(
                    [
                        "generate_pantographs_down_spritesheet",
                        "generate_pantographs_up_spritesheet",
                        "generate_buy_menu_sprite_vanilla_pantographs_down",
                        "generate_buy_menu_sprite_vanilla_pantographs_up",
                    ]
                )
            )
        self.num_pantograph_rows = len(self.catalogue)

    @property
    def nml_template(self):
        return "vehicle_engine.pynml"

    @property
    def variants_use_common_graphics_switch_chain(self):
        return False

    # get_output_row_types not re-implemented here as of July 2020, as no actual pixa processing is used for the engine sprites, add it if processing is needed in future


class GestaltGraphicsRandomisedWagon(GestaltGraphics):
    """
    Simple Gestalt specifically for randomised wagons that reuse action 2 graphics chains from other vehicles.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pipelines = pipelines.get_pipelines(
            [
                "generate_empty_spritesheet",
                "generate_buy_menu_sprite_from_randomisation_candidates",
            ]
        )
        self.dice_colour = kwargs["dice_colour"]
        self.buy_menu_width_addition = (
            graphics_constants.dice_image_width
            + 1
            + (2 * graphics_constants.randomised_wagon_extra_unit_width)
        )
        self.colour_mapping_switch = "_switch_colour_mapping"
        self.random_vehicle_map_type = kwargs["random_vehicle_map_type"]
        self.buy_menu_id_pairs = kwargs.get("buy_menu_id_pairs", None)
        # randomised buy menu sprites depend on generated vehicle spritesheet, so defer processing to round 2
        self.render_pass_num = 2

    @property
    def nml_template(self):
        return "vehicle_randomised.pynml"

    @property
    def variants_use_common_graphics_switch_chain(self):
        return True

    def buy_menu_row_map(self, pipeline):
        # for practicality we only want the default variant where variants exist,
        # e.g. no cc recoloured variants etc as it's seriously not worth handling those here
        wagon_randomisation_candidates = (
            pipeline.example_model_variant.wagon_randomisation_candidates
        )

        if self.buy_menu_id_pairs is not None:
            for candidate in wagon_randomisation_candidates:
                if candidate.model_id_root in self.buy_menu_id_pairs[0]:
                    candidate_1 = candidate
                    continue
                if candidate.model_id_root in self.buy_menu_id_pairs[1]:
                    candidate_2 = candidate
                    continue
            try:
                candidate_1
                candidate_2
            except:
                raise Exception(
                    f"{self.catalogue.model_id} \n"
                    f"Probably at least one of the candidates in buy_menu_id_pairs is not found. Options: \n"
                    f"- extend buy_menu_id_pairs with more types \n"
                    f"- this may not be a valid combo for this generation due to not actually having properly different candidates \n"
                    f"buy_menu_id_pairs: {self.buy_menu_id_pairs} \n"
                    f"wagon_randomisation_candidates: {[i.model_id_root for i in wagon_randomisation_candidates]} \n"
                )

        else:
            # we don't specify buy_menu_id_pair for simple cases e.g. livery randomisation of same base model
            # so this just slices out the first and last items of the list to make a pair of buy menu sprites
            # note that for randomised wagons, the list of candidates might be compile time non-deterministic
            # so the resulting sprites may vary between compiles - this is accepted as of August 2022
            candidate_1 = wagon_randomisation_candidates[0]
            candidate_2 = wagon_randomisation_candidates[-1]
            if pipeline.example_model_variant.badge_slug_randomised_wagon_type == "combo":
                print([i.model_id_root for i in wagon_randomisation_candidates])

        source_vehicles_and_input_spriterow_nums = [
            # vehicle unit, y offset (num spriterows) to buy menu input row
            # note that buy_menu_row_map works with *units*; we can always look up the model variant from the unit, but not trivially the other way round
            # candidate 1 and 2 are reversed for the compositor, this is just an implementation detail
            (
                candidate_2.units[0],
                0,
            ),
            (
                candidate_1.units[0],
                0,
            ),
        ]
        # buy menu sprite generation supports providing multiple variants (used for livery variants etc)
        # but here we only need one, in the default buy menu position
        result = [
            {
                "spriterow_num_dest": 0,
                "source_vehicles_and_input_spriterow_nums": source_vehicles_and_input_spriterow_nums,
            }
        ]
        return result


class GestaltGraphicsVisibleCargo(GestaltGraphics):
    """
    Used for vehicle with visible cargos
    Supports *only* pixa-generated cargos; mixing with custom cargo rows isn't handled, TMWFTLB
    Should not be used with 'random_reverse' property, composited cargos are symmetric, so cargo template doesn't handle random_reverse.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pipelines = pipelines.get_pipelines(
            [
                "extend_spriterows_for_composited_sprites_pipeline",
                "generate_buy_menu_sprite_vanilla_vehicle",
            ]
        )
        # default unweathered body recolour to CC1, pass param to override as needed
        # can optionally extend with "weathered" variant and an appropriate recolour map
        # (weathered state only used for non-CC body recolouring; CC will provide variants via recolour sprites automatically)
        self.weathered_states = kwargs.get(
            "weathered_states", {"unweathered": graphics_constants.body_recolour_CC1}
        )
        # possibly regrettable detection that weathered states should be implemented as a masked overlay sprite, in a spritelayer
        # this optimised file size and compile time, as don't have to repeat all cargo spriterows for the weathered state
        if "weathered" in self.weathered_states.keys():
            self.add_masked_overlay = True
        # cargo flags
        self.has_cover = kwargs.get("has_cover", False)
        self.has_bulk = kwargs.get("bulk", False)
        self.has_piece = kwargs.get("piece", None) is not None
        if self.has_piece:
            self.piece_type = kwargs.get("piece")

    @property
    def generic_rows(self):
        # map unknown cargos to sprites for some other label
        # assume that piece > input_spriterow_count, it's acceptable to show something like tarps for bulk, but not gravel for piece
        if self.has_piece:
            return self.cargo_row_map["DFLT"]
        elif self.has_bulk:
            return self.cargo_row_map["GRVL"]
        else:
            # shouldn't reach here, but eh,
            utils.echo_message("generic_rows hit an unknown result in GestaltGraphics")
            return ["FAIL"]

    @property
    def nml_template(self):
        return "vehicle_with_visible_cargo.pynml"

    @property
    def variants_use_common_graphics_switch_chain(self):
        return True

    def get_output_row_types(self):
        # note that this is *types* of rows, in order, not counts - counts are delegated elsehwere
        result = []
        # for e.g. tarpaulin cars, covered coil cars, insert a specific spriterow to show the cover when 100% loaded or travelling
        if self.has_cover:
            result.append("has_cover")
        # 1 empty spriterow
        result.append("empty")
        if self.has_bulk:
            result.append("bulk_cargo")
        if self.has_piece:
            result.append("piece_cargo")
        return result

    def get_generic_spriterow_output_variants(self, spriterow_type):
        # there may be variants of generic spriterows, to support weathered state, masked overlay etc
        result = []
        for variant_name, body_recolour_map in self.weathered_states.items():
            if spriterow_type == "has_cover":
                label = "COVERED"
                if variant_name == "weathered":
                    label = label + " - WEATHERED" + "\n" + "OVERLAY (NO MASK)"
                # no mask for covered rows, even if weathered
                mask_row_offset_count = None
            if spriterow_type == "empty":
                label = "EMPTY"
                if variant_name == "weathered":
                    # for this gestalt, weathered state is always implemented as a masked overlay
                    label = label + " - WEATHERED" + "\n" + "MASKED OVERLAY"
                    mask_row_offset_count = 1 + (2 * self.has_bulk) + self.has_piece
                else:
                    mask_row_offset_count = None
            result.append(
                {
                    "label": label,
                    "body_recolour_map": body_recolour_map,
                    "mask_row_offset_count": mask_row_offset_count,
                }
            )
        return result

    @cached_property
    def cargo_row_map(self):
        result = {}
        counter = 0
        if self.has_bulk:
            for cargo_map in polar_fox.constants.bulk_cargo_recolour_maps:
                result[cargo_map[0]] = [
                    counter
                ]  # list because a cargo label can map to multiple spriterows, but that is currently unused for visible cargo gestalt (June 2020)
                counter += 1
        if self.has_piece:
            # handle that piece cargos are defined in dicts as {filename:[labels]}, where most cargo sprite stuff uses ((label, values), (label, values)) pairs format
            for (
                cargo_filename
            ) in polar_fox.constants.piece_vehicle_type_to_sprites_maps[
                self.piece_type
            ]:
                for (
                    cargo_label
                ) in polar_fox.constants.piece_sprites_to_cargo_labels_maps[
                    cargo_filename
                ]:
                    result.setdefault(cargo_label, []).append(counter)
                counter += 1
        return result

    def get_unique_spritesets(self, unit):
        # the template for this gestalt was getting complex with loops and logic where logic shouldn't be
        # so instead we delegate that logic here and simplify the loop
        # this builds heavily on the row numbers already in cargo_row_map, reformatting that data to make it easy to render in the template
        row_nums_seen = []
        result = []
        for row_nums in self.cargo_row_map.values():
            for row_num in row_nums:
                row_nums_seen.append(row_num)
        unique_cargo_rows = set(row_nums_seen)

        row_height = graphics_constants.spriterow_height

        start_y_cumulative = graphics_constants.spritesheet_top_margin

        if self.has_cover:
            # add rows for covered sprite
            for weathered_state in self.weathered_states.keys():
                result.append(["has_cover_" + weathered_state, start_y_cumulative])
                start_y_cumulative += row_height

        # add rows for empty sprite
        for weathered_state in self.weathered_states.keys():
            result.append(["empty_" + weathered_state, start_y_cumulative])
            start_y_cumulative += row_height

        # !! not sure unique_cargo_rows order will always reliably match to what's needed, but if it doesn't, explicitly sort it eh
        for row_num in unique_cargo_rows:
            result.append(
                [
                    "loading_" + str(row_num),
                    start_y_cumulative,
                ]
            )
            result.append(
                [
                    "loaded_" + str(row_num),
                    start_y_cumulative + 30,
                ]
            )
            start_y_cumulative += 2 * row_height

        # vehicles with multiple units might need an offset to their sprites
        # to handle that we post-process the y-offsets in result
        # we make an assumption that the spriterows will always be vertically contiguous
        # so we can take the last value of start_y_cumulative, apply the offset multiplier, then rewrite the y values in result
        # n.b. by default force_spriterow_group_in_output_spritesheet = 0, so this has no effect unless explicitly set
        vehicle_y_offset = unit.unit_def.force_spriterow_group_in_output_spritesheet * (
            start_y_cumulative - graphics_constants.spritesheet_top_margin
        )
        for row_map in result:
            row_map[1] = row_map[1] + vehicle_y_offset
        return result

    def get_buy_menu_unit_input_row_num(
        self, pipeline, catalogue_entry, unit_counter, unit
    ):
        result = (
            len(self.get_unique_spritesets(unit))
            * unit.unit_def.force_spriterow_group_in_output_spritesheet
        )
        return result


class GestaltGraphicsBoxCarOpeningDoors(GestaltGraphics):
    """
    Used to handle the specific case of box-type freight cars
    - doors open during loading
    - no cargo is shown by design (TMWFTLB: piece sprites could be generated in, but setting up masks etc for all vehicles is unwanted complexity)
    """

    def __init__(self, weathered_states, **kwargs):
        super().__init__(**kwargs)
        self.pipelines = pipelines.get_pipelines(
            [
                "extend_spriterows_for_composited_sprites_pipeline",
                "generate_buy_menu_sprite_vanilla_vehicle",
            ]
        )
        # a default 'unweathered' variant must be provided
        # additional sets of recolour maps can be provided to generate 'weathered' sprites
        # these will be randomly selected in-game for visual variety
        # this is separate and complementary to the minor variations to vehicle company colours using in-game recolour sprites
        # there is no support here for weathered states that depend on hand-drawn pixels, it's all recolour maps as of March 2022 - could change if needed
        # note also that box cars have only one recolour map for *cargo*, which should be on 'DFLT',
        self.weathered_states = weathered_states

    @property
    def generic_rows(self):
        utils.echo_message(
            "generic_rows not implemented in GestaltGraphicsBoxCarOpeningDoorsGestaltGraphics (by design)"
        )
        return None

    @property
    def nml_template(self):
        return "vehicle_box_car_with_opening_doors.pynml"

    @property
    def variants_use_common_graphics_switch_chain(self):
        # !! could be common, but template looks to use unit.foo as of March 2025?
        return False

    def get_output_row_types(self):
        return ["box_car_with_opening_doors_spriterows"]

    @property
    def cargo_row_map(self):
        utils.echo_message(
            "cargo_row_map not implemented in GestaltGraphicsBoxCarOpeningDoorsGestaltGraphics (by design)"
        )
        return None

    def get_buy_menu_unit_input_row_num(
        self, pipeline, catalogue_entry, unit_counter, unit
    ):
        result = unit.rel_spriterow_index + (
            (catalogue_entry.livery_def.relative_spriterow_num)
            * self.num_load_state_or_similar_spriterows
        )
        return result


class GestaltGraphicsIntermodalContainerTransporters(GestaltGraphics):
    """
    Dedicated gestalt for intermodal container transporter
    Gestalt handles both
    - the model variant sprites
    - the spritelayer cargos which are in separate layer
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # we use the composited sprites pipeline so we can make use of chassis compositing
        self.pipelines = pipelines.get_pipelines(
            [
                "extend_spriterows_for_composited_sprites_pipeline",
                "generate_buy_menu_sprite_vanilla_vehicle",
            ]
        )
        # we need to run the spritelayer cargo pipelines separately from the vehicle pipelines, but we still use this gestalt as the entry point
        self.spritelayer_cargo_pipelines = pipelines.get_pipelines(
            ["generate_spritelayer_cargo_sets"]
        )
        self.colour_mapping_switch = "_switch_colour_mapping"
        self.colour_mapping_with_purchase = False
        # add layers for container sprites
        # !! this might need extended for double stacks in future - see automobile gestalt for examples of deriving this from number of cargo sprite layers
        self.num_extra_layers_for_spritelayer_cargos = 1
        # the actual containers are symmetric
        self.cargo_sprites_are_asymmetric = False
        # intermodal cars are asymmetric, sprites are drawn in second col, first col needs populated, map is [col 1 dest]: [col 2 source]
        # two liveries
        self.asymmetric_row_map = {
            1: 1,
            2: 3,  # default: default
            3: 2,
            4: 4,  # first: last
        }

    def get_output_row_types(self):
        # 2 liveries * 4 formation position rules so 8 empty rows, we're only using the composited sprites pipeline for chassis compositing, containers are provided on separate layer
        # note to self, remarkably adding multiple empty rows appears to just work here :o
        return ["empty", "empty", "empty", "empty"]

    def get_generic_spriterow_output_variants(self, spriterow_type):
        # there may be variants of generic spriterows, to support weathered state, masked overlay etc
        # for this gestalt, it's just one empty output row per input row, no other variants
        if spriterow_type != "empty":
            # only empty rows are supported eh
            raise BaseException(
                "get_generic_spriterow_output_variants only supports 'empty' as spriterow_type, and may need extending"
            )
        result = []
        result.append(
            {
                "label": "EMPTY",
                "body_recolour_map": None,
                "mask_row_offset_count": None,
            }
        )
        return result

    def allow_adding_cargo_label(self, cargo_label, container_type, result):
        # don't ship DFLT as actual cargo label, it's not a valid cargo and will cause nml to barf
        # the generation of the DFLT container sprites is handled separately without using cargo_label_mapping
        if cargo_label == "DFLT":
            return False
        # explicit control over contested cargo_labels, by specifying which container type should be used (there can only be one type for label based support)
        contested_cargo_labels = {
            "CHLO": "cryo_tank",
            "FOOD": "reefer",
            "N7__": "cryo_tank",
            "RFPR": "chemicals_tank",
            "SULP": "tank",
        }
        if cargo_label in contested_cargo_labels.keys():
            if container_type == contested_cargo_labels[cargo_label]:
                return True
            else:
                return False
        # print a note if an unhandled contested cargo is found, so the contested cargos can be updated to handle the cargo label
        if cargo_label in result:
            print(
                "GestaltGraphicsIntermodalContainerTransporters.cargo_label_mapping: cargo_label",
                cargo_label,
                "already exists, being over-written by",
                container_type,
                "label; update contested_cargo_labels in gestalt_graphics",
            )
        # default to allowing, most cargos aren't contested
        return True

    @cached_property
    def cargo_label_mapping(self):
        result = {}
        for (
            container_type,
            cargo_maps,
        ) in polar_fox.constants.container_recolour_cargo_maps:
            # first handle the cargos as explicitly refittable
            # lists of explicitly refittable cargos are by no means *all* the cargos refittable to for a type
            # nor does explicitly refittable cargos have 1:1 mapping with cargo-specific graphics
            # the mapping expected by spritelayer cargos is cargo_label: (subtype, subtype_suffix)
            # these will all map cargo_label: (container_type, DFLT)
            for cargo_label in cargo_maps[0]:
                if self.allow_adding_cargo_label(cargo_label, container_type, result):
                    result[cargo_label] = (container_type, "DFLT")

            # then insert or override entries with cargo_label: (container_type, [CARGO_LABEL]) where there are explicit graphics for a cargo
            for cargo_label, recolour_map in cargo_maps[1]:
                if self.allow_adding_cargo_label(cargo_label, container_type, result):
                    result[cargo_label] = (container_type, cargo_label)
        # special handling of flatracks with visible cargo sprites
        for cargo_list in polar_fox.constants.container_piece_cargo_maps.values():
            for cargo_label in cargo_list:
                if self.allow_adding_cargo_label(cargo_label, "stake_flatrack", result):
                    result[cargo_label] = ("stake_flatrack", cargo_label)
        return result

    @cached_property
    def formation_position_labels(self):
        # used in spriteset templating
        if self.formation_ruleset == "max_1_unit_sets":
            # 1 unit articulated sets only need 1 position rule
            return ["default"]
        elif self.formation_ruleset == "max_2_unit_sets":
            # 2 unit articulated sets only need 3 position rules
            return ["default", "first", "last"]
        else:
            return ["default", "first", "last", "middle"]

    @property
    def nml_template(self):
        # override in subclasses as needed
        return "vehicle_intermodal.pynml"

    @property
    def variants_use_common_graphics_switch_chain(self):
        return False


class GestaltGraphicsAutomobilesTransporter(GestaltGraphics):
    """
    Dedicated automobiles (car, truck, tractor) transporter
    Gestalt handles both
    - the model variant sprites
    - the spritelayer cargos which are in separate layer
    """

    def __init__(self, spritelayer_cargo_layers=["default"], **kwargs):
        super().__init__(**kwargs)
        self.add_masked_overlay = kwargs.get("add_masked_overlay", False)
        # we use the composited sprites pipeline so we can make use of chassis compositing
        self.pipelines = pipelines.get_pipelines(
            [
                "extend_spriterows_for_composited_sprites_pipeline",
                "generate_buy_menu_sprite_vanilla_vehicle",
            ]
        )
        # we need to run the spritelayer cargo pipelines separately from the vehicle pipelines, but we still use this gestalt as the entry point
        self.spritelayer_cargo_pipelines = pipelines.get_pipelines(
            ["generate_spritelayer_cargo_sets"]
        )
        self.colour_mapping_switch = "_switch_colour_mapping"
        self.colour_mapping_with_purchase = False
        self.cargo_sprites_are_asymmetric = True
        # derive number of layers for cargo sprites
        self.num_extra_layers_for_spritelayer_cargos = len(spritelayer_cargo_layers)

    def get_output_row_types(self):
        # !! the actual number of variants needs decided - are we having articulated variants or just single units?
        # 2 liveries * 4 formation position rules, so 8 empty rows, we're only using the composited sprites pipeline for chassis compositing, containers are provided on separate layer
        # note to self, remarkably adding multiple empty rows appears to just work here :o
        if self.formation_ruleset == "max_1_unit_sets":
            result = ["empty"]
        elif self.formation_ruleset == "max_2_unit_sets":
            result = [
                "empty",
                "empty",
                "empty",
            ]
        elif self.formation_ruleset == "max_4_unit_sets":
            result = [
                "empty",
                "empty",
                "empty",
                "empty",
            ]
        else:
            raise BaseException(
                str(self.formation_ruleset)
                + " not matched in GestaltGraphicsAutomobilesTransporter get_output_row_types()"
            )
        if self.add_masked_overlay:
            temp_result = []
            for row_type in result:
                # we want to skip the a row as it will just contain a mask, setting row_type to None seems to work fine
                temp_result.append(row_type)
                temp_result.append(None)
            result = temp_result
        return result

    def get_generic_spriterow_output_variants(self, spriterow_type):
        # there may be variants of generic spriterows, to support weathered state, masked overlay etc
        # for this gestalt, it's just one empty output row per input row, no other variants
        if spriterow_type != "empty":
            # only empty rows are supported eh
            raise BaseException(
                "get_generic_spriterow_output_variants only supports 'empty' as spriterow_type, and may need extending"
            )
        result = []
        result.append(
            {
                "label": "BASE PLATFORM",
                "body_recolour_map": None,
                "mask_row_offset_count": None,
            }
        )
        if self.add_masked_overlay:
            result.append(
                {
                    "label": "MASKED OVERLAY",
                    "body_recolour_map": None,
                    "mask_row_offset_count": 1,
                }
            )
        return result

    @property
    def vehicle_spritelayer_names(self):
        result = ["base_platform"]
        if self.add_masked_overlay:
            result.append("masked_overlay")
        return result

    def get_unique_spritesets(self, unit):
        # the template for this gestalt was getting complex with loops and logic where logic shouldn't be
        # so instead we delegate that logic here and simplify the loop
        row_height = graphics_constants.spriterow_height

        result = []
        start_y_cumulative = graphics_constants.spritesheet_top_margin

        # add rows for empty sprite
        for label in self.formation_position_labels:
            for vehicle_spritelayer_name in self.vehicle_spritelayer_names:
                result.append(
                    [
                        vehicle_spritelayer_name + "_" + label,
                        start_y_cumulative,
                    ]
                )
                start_y_cumulative += row_height
        return result

    @property
    def cargo_label_mapping(self):
        result = {}
        # see intermodal for example of how this mapped containers
        # for vehicles this maybe just needs to switch e.g on cargo subtype or something - trucks, cars etc
        return result

    @cached_property
    def formation_position_labels(self):
        # used in spriteset templating
        if self.formation_ruleset == "articulated_permanent_twin_sets":
            # permanent articulated twin sets only need 2 formation position rules
            return ["first", "last"]
        elif self.formation_ruleset == "max_1_unit_sets":
            # 1 unit articulated sets only need 1 position rule
            return ["default"]
        elif self.formation_ruleset == "max_2_unit_sets":
            # 2 unit articulated sets only need 3 position rules
            return ["default", "first", "last"]
        else:
            # defaulting to 4 unit sets is apparently fine?
            return ["default", "first", "last", "middle"]

    @property
    def nml_template(self):
        # override in subclasses as needed
        return "vehicle_automobile_car.pynml"

    @property
    def variants_use_common_graphics_switch_chain(self):
        return False


class GestaltGraphicsSimpleBodyColourRemaps(GestaltGraphics):
    """
    Simple recolouring from false body colour to a single default livery
    Recolouring from false body colour makes it easy to adjust base liveries across all vehicles of the same type.
    This gestalt can also be used as a shortcut simply for adding automated chassis.
    """

    def __init__(self, weathered_states, **kwargs):
        super().__init__(**kwargs)
        self.pipelines = pipelines.get_pipelines(
            [
                "extend_spriterows_for_composited_sprites_pipeline",
                "generate_buy_menu_sprite_vanilla_vehicle",
            ]
        )
        # recolour_maps map cargo labels to liveries, use 'DFLT' as the labe in the case of just one livery
        # a default 'unweathered' variant must be provided
        # additional sets of recolour maps can be provided to generate 'weathered' sprites
        # if cargo recolours are provided weathered and unweathered MUST provide the same cargo support
        # these will be randomly selected in-game for visual variety
        # this is separate and complementary to the minor variations to vehicle company colours using in-game recolour sprites
        # there is no support here for weathered states that depend on hand-drawn pixels, it's all recolour maps as of March 2022 - could change if needed
        self.weathered_states = weathered_states

    @property
    def generic_rows(self):
        utils.echo_message(
            "generic_rows not implemented in GestaltGraphicsSimpleBodyColourRemaps (by design)"
        )
        return None

    @property
    def nml_template(self):
        return "vehicle_with_simple_body_colour_remaps.pynml"

    @property
    def variants_use_common_graphics_switch_chain(self):
        return True

    def get_output_row_types(self):
        return ["simple_recolour_spriterows"]


class GestaltGraphicsFormationDependent(GestaltGraphics):
    """
     Used when the vehicle changes appearance depending on position in the formation
     Intended for pax and mail cars
      - intended for closed vehicles with doors, 'loaded' sprites are same as 'empty'
      - option to show loading sprites (open doors) via 1 or 2 'loading' rows
    - vehicles can be configured to optionally show 1 of 4 different sprites depending on position in formation
         - 'default'
         - 'first'
         - 'last'
         - 'special'
     - 'positions' are flexible, and hax can safely be used within reason to get worthwhile results / save time
         - positions are controlled by formation_rulesets, defined per model type as needed
         - the positions are just keywords, mapped onto spriterow nums, and can be remapped fairly freely
     - the limit of 4 is arbitrary, and self-imposed to prevent combinatorial explosion (and consequent need to draw sprites)
    """

    def __init__(self, formation_position_spriterow_map, **kwargs):
        super().__init__(**kwargs)
        # formation_position_spriterow_map provided by subclass calling gestalt_graphics:
        # - spriterow numbers for named positions in formation
        # - spriterow numbers are zero-indexed *relative* to the start of the formation-cargo block, to reduce shuffling them all if new rows are inserted in future
        # - *all* of the keys must be provided in the mapping, set values to 0 if unused
        self.formation_position_spriterow_map = formation_position_spriterow_map
        # we'll generate spriterows for doors closed and doors open
        self.num_load_state_or_similar_spriterows = 2
        # colour mapping stuff...
        self.colour_mapping_switch = "_switch_colour_mapping"
        self.colour_mapping_switch_purchase = "_switch_colour_mapping"
        self.colour_mapping_with_purchase = True
        # verify that the formation_position_spriterow_map keys are in the expected order
        if list(self.formation_position_spriterow_map.keys()) != [
            "default",
            "first",
            "last",
            "special",
        ]:
            raise BaseException(
                "Keys aren't correct for formation_position_spriterow_map: "
                + str(formation_position_spriterow_map)
            )
        # configure pipelines
        self.pipelines = pipelines.get_pipelines(
            [
                "extend_spriterows_for_composited_sprites_pipeline",
                "generate_buy_menu_sprite_vanilla_vehicle",
            ]
        )
        # add pantographs as necessary
        if kwargs.get("pantograph_type", None) is not None:
            self.pipelines.extend(
                pipelines.get_pipelines(
                    [
                        "generate_pantographs_down_spritesheet",
                        "generate_pantographs_up_spritesheet",
                        "generate_buy_menu_sprite_vanilla_pantographs_down",
                        "generate_buy_menu_sprite_vanilla_pantographs_up",
                    ]
                )
            )
            # this assumes no gaps in the spriterows, so take the max spriterow num
            # note the +1 because livery rows are zero indexed
            # note that we simply generate a row per formation position
            # this method leads to unnecessary rows for many cases
            # but is relied on for multiple unit (railcars etc) where not all vehicles have pans, in which case the row is simply empty
            self.num_pantograph_rows = len(self.catalogue) * (
                1 + max(self.formation_position_spriterow_map.values())
            )

    @property
    def nml_template(self):
        # override in subclasses as needed
        return "vehicle_formation_position_dependent.pynml"

    @property
    def variants_use_common_graphics_switch_chain(self):
        return False

    def get_output_row_types(self):
        return ["pax_mail_cars_with_doors"]

    @cached_property
    def num_spritesheet_liveries_per_formation_position(self):
        return len(self.catalogue)

    @cached_property
    def total_spriterow_count(self):
        # n unique liveries * 2 states for doors open/closed * number of formation position rules defined
        return (
            self.num_spritesheet_liveries_per_formation_position
            * self.num_load_state_or_similar_spriterows
            * self.num_unique_formation_positions
        )

    @cached_property
    def num_unique_formation_positions(self):
        # rows can be reused across multiple formation position labels, so find uniques
        return len(set(list(self.formation_position_spriterow_map.values())))

    @cached_property
    def asymmetric_row_map(self):
        # used in graphics processor to figure out how to make correct asymmetric sprites for 'first' and 'last'
        # pax / mail cars are asymmetric, sprites are drawn in second col, first col needs populated, map is [col 1 dest]: [col 2 source]
        result = {}
        base_row_num = 0
        # This is tied completely to the spritesheet format:
        # [1..4] formation positions x n liveries x 2 rows (empty & loaded, loading)
        # note that formation_position_num is index in unique position rules *not* index in the formation
        for formation_position_num in range(self.num_unique_formation_positions):
            if formation_position_num == self.formation_position_spriterow_map["first"]:
                source_row_num = self.formation_position_spriterow_map["last"]
            elif (
                formation_position_num == self.formation_position_spriterow_map["last"]
            ):
                source_row_num = self.formation_position_spriterow_map["first"]
            else:
                source_row_num = formation_position_num
            # group of n rows - n liveries * two loaded/loading states (opening doors)
            row_group_size = self.num_load_state_or_similar_spriterows * len(
                self.catalogue
            )
            for i in range(1, 1 + row_group_size):
                result[base_row_num + (row_group_size * formation_position_num) + i] = (
                    base_row_num + (row_group_size * source_row_num) + i
                )
        return result

    def get_buy_menu_unit_input_row_num(
        self, pipeline, catalogue_entry, unit_counter, unit
    ):
        # as of Jan 2024 it was easiest to enforce that this only works with model variant comprised of exactly 2 units
        # that means we can just do first / last, and not worry about other formation positions
        # support for arbitrary number of units could be added, derived from formation ruleset, but those cases don't exist as of Jan 2024
        if len(pipeline.example_model_variant.units) != 2:
            if pipeline.example_model_variant.id == "golfinho":
                # JFDI jank
                if unit_counter == 1:
                    formation_position_row_offset = (
                        self.formation_position_spriterow_map["special"]
                    )
                    result = (
                        self.num_spritesheet_liveries_per_formation_position
                        * formation_position_row_offset
                        * self.num_load_state_or_similar_spriterows
                    ) + (
                        catalogue_entry.livery_def.relative_spriterow_num
                        * self.num_load_state_or_similar_spriterows
                    )
                    return result
            else:
                raise BaseException(
                    "GestaltGraphicsFormationDependent.get_buy_menu_unit_input_row_num(): catalogue "
                    + pipeline.catalogue.model_id
                    + " does not have exactly 2 units - this case is not currently supported"
                )

        if unit_counter == 0:
            formation_position_row_offset = self.formation_position_spriterow_map[
                "first"
            ]
        else:
            formation_position_row_offset = self.formation_position_spriterow_map[
                "last"
            ]
        if pipeline.is_pantographs_pipeline:
            result = formation_position_row_offset
        else:
            result = (
                self.num_spritesheet_liveries_per_formation_position
                * formation_position_row_offset
                * self.num_load_state_or_similar_spriterows
            ) + (
                catalogue_entry.livery_def.relative_spriterow_num
                * self.num_load_state_or_similar_spriterows
            )

        return result


class GestaltGraphicsCustom(GestaltGraphics):
    """
    Used to handle (rare) cases with hand-drawn cargo or no cargo (no pixa-generated cargos).
    There is currently no graphics processing for this:
    - just a simple pass-through, and an interface to the nml templates
    - this could get support for body recolouring if needed
    - this should not get support for compositing custom rows, TMWFTLB, just draw them in the vehicle spritesheet
    """

    def __init__(
        self,
        _nml_template,
        variants_use_common_graphics_switch_chain=None,
        cargo_row_map=None,
        generic_rows=None,
        unique_spritesets=None,
        cargo_label_mapping=None,
        weathered_states=None,
        num_extra_layers_for_spritelayer_cargos=None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.pipelines = pipelines.get_pipelines(["pass_through_pipeline"])
        self._nml_template = _nml_template
        self._variants_use_common_graphics_switch_chain = (
            variants_use_common_graphics_switch_chain
        )
        self._cargo_row_map = cargo_row_map
        self._generic_rows = generic_rows
        self._unique_spritesets = unique_spritesets
        self._cargo_label_mapping = cargo_label_mapping
        self._weathered_states = weathered_states
        if num_extra_layers_for_spritelayer_cargos is not None:
            self.num_extra_layers_for_spritelayer_cargos = (
                num_extra_layers_for_spritelayer_cargos
            )

    @property
    def generic_rows(self):
        # generic rows is normally automated, but for custom, get it from a manully specified property
        return self._generic_rows

    @property
    def nml_template(self):
        return self._nml_template

    @property
    def variants_use_common_graphics_switch_chain(self):
        if self._variants_use_common_graphics_switch_chain is not None:
            return self._variants_use_common_graphics_switch_chain
        else:
            return False

    def get_output_row_types(self):
        return ["custom_cargo"]

    @property
    def cargo_row_map(self):
        return self._cargo_row_map

    def get_unique_spritesets(self, unit):
        return self._unique_spritesets

    @property
    def cargo_label_mapping(self):
        return self._cargo_label_mapping

    def buy_menu_row_map(self, pipeline):
        # not implemented as of Jan 2024 - provide custom buy menu sprites via the template and/or manually in the spritesheet
        raise BaseException(
            "buy_menu_row_map called in GestaltGraphicsCustom for catalogue "
            + pipeline.catalogue.model_id
            + " - this isn't supported."
        )

    @property
    def weathered_states(self):
        if self._weathered_states == None:
            # provide a default weathered_state to spriteset templating, iff the template wants this attribute
            return {"unweathered": {}}
        else:
            return self._weathered_states
