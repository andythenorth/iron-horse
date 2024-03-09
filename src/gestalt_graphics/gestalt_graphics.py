import polar_fox
import gestalt_graphics.graphics_constants as graphics_constants
from gestalt_graphics import pipelines
import utils

# get args passed by makefile
command_line_args = utils.get_command_line_args()


class GestaltGraphics(object):
    """
    Simple class, which is extended in subclasses to configure:
     - base vehicle recolour (if any)
     - cargo graphics (if any)
     - pantographs (if any)
     - other processing as required
    """

    def __init__(self, **kwargs):
        # by default, pipelines are empty
        self.pipelines = pipelines.get_pipelines([])
        # sometimes processing may depend on another generated vehicle spritesheet, so there are multiple processing priorities, 1 = highest
        self.processing_priority = 1
        # default value for optional mask layer, this is JFDI for 2022, may need converting a more generic spritelayers structure in future
        # set directly by the consist self.gestalt_graphics.add_masked_overlay = True, or by kwargs on a specific gestalt subclass
        self.add_masked_overlay = False
        self.buy_menu_width_addition = 0
        # override this in subclasses as needed
        self.num_load_state_or_similar_spriterows = 1
        # optional - rulesets are used to define for different types of vehicle how sprites change depending on consist position
        # ruleset may also be used for buy menu sprite processing
        self.consist_ruleset = kwargs.get("consist_ruleset", None)
        # optional - (not common) we can delegate to another spritesheet if we're doing e.g. different consist types, but recolouring the same base sprites
        self.input_spritesheet_delegate_id = kwargs.get(
            "input_spritesheet_delegate_id", None
        )
        # !! we need a way to get a useful (if not perfect) debug vehicle image for checking pantograph positions, and this lets us force useful rows for vehicle and pan
        self.jfdi_pantograph_debug_image_y_offsets = kwargs.get(
            "jfdi_pantograph_debug_image_y_offsets", [0, 0]
        )

    @property
    def nml_template(self):
        # override in subclasses as needed
        # return a pnml file name, e.g. `return 'vehicle_default.pynml'`
        return None

    def get_output_row_types(self):
        # stub, for compatibility reasons
        return ["single_row"]

    @property
    def all_liveries(self):
        # stub to map this gestalt's liveries to the wider all_liveries structure
        # this can be over-ridden as needed by gestalts
        # note that self.liveries must be initialised by passing a keyword (as the default livery comes from the roster which is not in scope here)
        # if self.liveries is undefined, that's an error
        return self.liveries

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
            # pans are the same for all buyable variants, and are just provided either once, or per position variant
            dest_spriterows = pipeline.consist.buyable_variants[0:1]
        else:
            dest_spriterows = pipeline.consist.buyable_variants
        for dest_spriterow_counter, buyable_variant in enumerate(dest_spriterows):
            source_vehicles_and_input_spriterow_nums = []

            for unit_counter, unit in enumerate(pipeline.consist.units):
                # vehicle unit, y offset (num spriterows) to buy menu input row
                source_vehicles_and_input_spriterow_nums.append(
                    [
                        unit,
                        self.get_buy_menu_unit_input_row_num(
                            unit_counter, pipeline, buyable_variant, unit
                        ),
                    ]
                )

            # buyable_variant_counter maps to spriterow_num_dest
            # the spritesheet has buy menu sprites in their own descending vertical order corresponding to buyable variants
            # the custom buy menu sprites don't align vertically with any specific vehicle spriterow and have dedicated nml templating
            row_config = {
                "spriterow_num_dest": dest_spriterow_counter,
                "source_vehicles_and_input_spriterow_nums": source_vehicles_and_input_spriterow_nums,
            }
            result.append(row_config)
        return result

    def get_buy_menu_unit_input_row_num(
        self, unit_counter, pipeline, buyable_variant, unit
    ):
        # override in subclasses as needed

        # !! isn't this already known somewhere?  Gestalts might be counting liveries already
        # ?? self.num_load_state_or_similar_spriterows on the gestalt?
        if pipeline.consist.gestalt_graphics.__class__.__name__ in [
            "GestaltGraphicsBoxCarOpeningDoors"
        ]:
            num_livery_rows_per_unit = 1
        else:
            num_livery_rows_per_unit = len(pipeline.consist.buyable_variants)

        # !! CABBAGE - this needs to delegate to consist_ruleset, to find, e.g. an additional y offset to the spriterow for 'first' or 'last' etc
        if pipeline.consist.id in ["sliding_wall_car_pony_gen_5D"]:
            print(pipeline.consist.id)
            print(unit_counter)
            print("--- ^ buy menu spriterow y offset debug ---")

        unit_variant_row_num = (unit.spriterow_num * num_livery_rows_per_unit) + (
            (buyable_variant.relative_spriterow_num)
            * self.num_load_state_or_similar_spriterows
        )
        return unit_variant_row_num


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
        self.liveries = kwargs["liveries"]
        self.default_livery_extra_docs_examples = kwargs.get(
            "default_livery_extra_docs_examples", []
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
        self.num_pantograph_rows = len(self.liveries)

    @property
    def nml_template(self):
        return "vehicle_engine.pynml"

    # get_output_row_types not re-implemented here as of July 2020, as no actual pixa processing is used for the engine sprites, add it if processing is needed in future


class GestaltGraphicsRandomisedWagon(GestaltGraphics):
    """
    Simple Gestalt specifically for randomised wagons that have borrow sprites from other vehicles.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pipelines = pipelines.get_pipelines(
            [
                "generate_empty_spritesheet",
                "generate_buy_menu_sprite_from_randomisation_candidates",
            ]
        )
        self.liveries = kwargs["liveries"]
        self.dice_colour = kwargs["dice_colour"]
        self.buy_menu_width_addition = (
            graphics_constants.dice_image_width
            + 1
            + (2 * graphics_constants.randomised_wagon_extra_unit_width)
        )
        self.colour_mapping_switch = "_switch_colour_mapping"
        self.colour_mapping_switch_purchase = "_switch_colour_mapping_purchase"
        self.colour_mapping_with_purchase = True
        # randomised buy menu sprites depend on generated vehicle spritesheet, so defer processing to round 2
        self.processing_priority = 2

    @property
    def nml_template(self):
        return "vehicle_randomised.pynml"

    def buy_menu_row_map(self, pipeline):
        # for practicality we only want the default variant where variants exist,
        # e.g. no cc recoloured variants etc as it's seriously not worth handling those here
        candidate_consists = []
        for unit_variant in pipeline.consist.frozen_roster_items[
            "wagon_randomisation_candidates"
        ][0]:
            # ^^^ !! picking the first item off is hax
            if unit_variant.unit.consist not in candidate_consists:
                candidate_consists.append(unit_variant.unit.consist)
        # this appears to just slice out the first two items of the list to make a pair of buy menu sprites
        # note that for randomised wagons, the list of candidates is compile time non-deterministic
        # so the resulting sprites may vary between compiles - this is accepted as of August 2022
        source_vehicles_and_input_spriterow_nums = [
            # vehicle unit, y offset (num spriterows) to buy menu input row
            # note that buy_menu_row_map works with *units* not consists; we can always look up the consist from the unit, but not trivially the other way round
            (
                list(candidate_consists)[0].units[0],
                0,
            ),
            (
                list(candidate_consists)[1].units[0],
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
        # (weathered variant only used for non-CC body recolouring; CC will provide variants via recolour sprites automatically)
        self.weathered_variants = kwargs.get(
            "weathered_variants", {"unweathered": graphics_constants.body_recolour_CC1}
        )
        self.liveries = kwargs["liveries"]
        # possibly regrettable detection that weathered variants should be implemented as a masked overlay sprite, in a spritelayer
        # this optimised file size and compile time, as don't have to repeat all cargo spriterows for the weathered variant
        if "weathered" in self.weathered_variants.keys():
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
        # there may be variants of generic spriterows, to support weathered variant, masked overlay etc
        result = []
        for variant_name, body_recolour_map in self.weathered_variants.items():
            if spriterow_type == "has_cover":
                label = "COVERED"
                if variant_name == "weathered":
                    label = label + " - WEATHERED" + "\n" + "OVERLAY (NO MASK)"
                # no mask for covered rows, even if weathered
                mask_row_offset_count = None
            if spriterow_type == "empty":
                label = "EMPTY"
                if variant_name == "weathered":
                    # for this gestalt, weathered variant is always implemented as a masked overlay
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

    @property
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

    @property
    def unique_spritesets(self):
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
            for weathered_variant in self.weathered_variants.keys():
                result.append(["has_cover_" + weathered_variant, start_y_cumulative])
                start_y_cumulative += row_height

        # add rows for empty sprite
        for weathered_variant in self.weathered_variants.keys():
            result.append(["empty_" + weathered_variant, start_y_cumulative])
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
        return result


class GestaltGraphicsBoxCarOpeningDoors(GestaltGraphics):
    """
    Used to handle the specific case of box-type freight cars
    - doors open during loading
    - no cargo is shown by design (TMWFTLB: piece sprites could be generated in, but setting up masks etc for all vehicles is unwanted complexity)
    """

    def __init__(self, weathered_variants, **kwargs):
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
        # there is no support here for weathered variants that depend on hand-drawn pixels, it's all recolour maps as of March 2022 - could change if needed
        # note also that box cars have only one recolour map for *cargo*, which should be on 'DFLT',
        self.weathered_variants = weathered_variants
        self.liveries = kwargs["liveries"]

    @property
    def generic_rows(self):
        utils.echo_message(
            "generic_rows not implemented in GestaltGraphicsBoxCarOpeningDoorsGestaltGraphics (by design)"
        )
        return None

    @property
    def nml_template(self):
        return "vehicle_box_car_with_opening_doors.pynml"

    def get_output_row_types(self):
        return ["box_car_with_opening_doors_spriterows"]

    @property
    def cargo_row_map(self):
        utils.echo_message(
            "cargo_row_map not implemented in GestaltGraphicsBoxCarOpeningDoorsGestaltGraphics (by design)"
        )
        return None


class GestaltGraphicsCaboose(GestaltGraphics):
    """
    Used to handle specific rules for caboose cars
    - colour remap
    - specific livery variants (pixels, not just colour remap) for specific engine IDs
    """

    def __init__(
        self,
        recolour_map,
        spriterow_labels,
        caboose_families,
        buy_menu_sprite_pairs,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.pipelines = pipelines.get_pipelines(
            [
                "extend_spriterows_for_composited_sprites_pipeline",
                "generate_buy_menu_sprite_from_randomisation_candidates",
            ]
        )
        self.spriterow_labels = spriterow_labels
        self.caboose_families = caboose_families
        self.buy_menu_sprite_pairs = buy_menu_sprite_pairs
        self.num_variations = len(self.spriterow_labels)
        self.recolour_map = recolour_map
        self.liveries = kwargs["liveries"]
        self.dice_colour = 1
        self.buy_menu_width_addition = (
            graphics_constants.dice_image_width
            + 1
            + (2 * graphics_constants.randomised_wagon_extra_unit_width)
        )

    @property
    def generic_rows(self):
        utils.echo_message(
            "generic_rows not implemented in GestaltGraphicsCaboose (by design)"
        )
        return None

    @property
    def nml_template(self):
        return "vehicle_caboose.pynml"

    def get_output_row_types(self):
        return ["caboose_spriterows"]

    @property
    def cargo_row_map(self):
        utils.echo_message(
            "cargo_row_map not implemented in GestaltGraphicsCaboose (by design)"
        )
        return None

    def buy_menu_row_map(self, pipeline):
        result = []
        for counter, buy_menu_sprite_pair in enumerate(self.buy_menu_sprite_pairs):
            row_config = {"spriterow_num_dest": counter}
            # vehicle unit, y offset (num spriterows) to buy menu input row
            # note that buy_menu_row_map works with *units* not consists; we can always look up the consist from the unit, but not trivially the other way round
            source_vehicles_and_input_spriterow_nums = [
                (
                    pipeline.consist.units[0],
                    self.spriterow_labels.index(buy_menu_sprite_pair[0]),
                ),
                (
                    pipeline.consist.units[0],
                    self.spriterow_labels.index(buy_menu_sprite_pair[1]),
                ),
            ]

            row_config["source_vehicles_and_input_spriterow_nums"] = (
                source_vehicles_and_input_spriterow_nums
            )
            result.append(row_config)
        return result


class GestaltGraphicsIntermodalContainerTransporters(GestaltGraphics):
    """
    Dedicated gestalt for intermodal container transporter
    Gestalt handles both
    - the consist sprites
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
        self.liveries = kwargs["liveries"]
        # add layers for container sprites
        # !! this might need extended for double stacks in future - see automobile gestalt for examples of deriving this from number of cargo sprite layers
        self.num_extra_layers_for_spritelayer_cargos = 1
        # the actual containers are symmetric
        self.cargo_sprites_are_asymmetric = False
        # intermodal cars are asymmetric, sprites are drawn in second col, first col needs populated, map is [col 1 dest]: [col 2 source]
        # two liveries
        self.asymmetric_row_map = {
            1: 1,
            2: 2,  # default: default
            3: 5,
            4: 6,  # first: last
            5: 3,
            6: 4,  # last: first
            7: 7,
            8: 8,  # middle: middle
        }

    def get_output_row_types(self):
        # 2 liveries * 4 variants so 8 empty rows, we're only using the composited sprites pipeline for chassis compositing, containers are provided on separate layer
        # note to self, remarkably adding multiple empty rows appears to just work here :o
        return ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]

    def get_generic_spriterow_output_variants(self, spriterow_type):
        # there may be variants of generic spriterows, to support weathered variant, masked overlay etc
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

    @property
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

    @property
    def position_variants(self):
        # used in spriteset templating
        if self.consist_ruleset == "1_unit_sets":
            # 1 unit articulated sets only need 1 variant
            return ["default"]
        elif self.consist_ruleset == "2_unit_sets":
            # 2 unit articulated sets only need 3 variants
            return ["default", "first", "last"]
        else:
            return ["default", "first", "last", "middle"]

    @property
    def nml_template(self):
        # override in subclasses as needed
        return "vehicle_intermodal.pynml"


class GestaltGraphicsAutomobilesTransporter(GestaltGraphics):
    """
    Dedicated automobiles (car, truck, tractor) transporter
    Gestalt handles both
    - the consist sprites
    - the spritelayer cargos which are in separate layer
    """

    def __init__(self, spritelayer_cargo_layers=["default"], **kwargs):
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
        self.cargo_sprites_are_asymmetric = True
        self.liveries = kwargs["liveries"]
        # derive number of layers for cargo sprites
        self.num_extra_layers_for_spritelayer_cargos = len(spritelayer_cargo_layers)

    def get_output_row_types(self):
        # !! the actual number of variants needs decided - are we having articulated variants or just single units?
        # 2 liveries * 4 variants so 8 empty rows, we're only using the composited sprites pipeline for chassis compositing, containers are provided on separate layer
        # note to self, remarkably adding multiple empty rows appears to just work here :o
        if self.consist_ruleset == "1_unit_sets":
            result = ["empty"]
        elif self.consist_ruleset == "4_unit_sets":
            result = [
                "empty",
                "empty",
                "empty",
                "empty",
            ]
        else:
            raise BaseException(
                str(self.consist_ruleset)
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
        # there may be variants of generic spriterows, to support weathered variant, masked overlay etc
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

    @property
    def unique_spritesets(self):
        # the template for this gestalt was getting complex with loops and logic where logic shouldn't be
        # so instead we delegate that logic here and simplify the loop
        row_height = graphics_constants.spriterow_height

        result = []
        start_y_cumulative = graphics_constants.spritesheet_top_margin

        # add rows for empty sprite
        for variant in self.position_variants:
            for vehicle_spritelayer_name in self.vehicle_spritelayer_names:
                result.append(
                    [
                        vehicle_spritelayer_name + "_" + variant,
                        start_y_cumulative,
                    ]
                )
                start_y_cumulative += row_height
        return result

    """
    def allow_adding_cargo_label(self, cargo_label, container_type, result):
        # don't ship DFLT as actual cargo label, it's not a valid cargo and will cause nml to barf
        # the generation of the DFLT container sprites is handled separately without using cargo_label_mapping
        if cargo_label == "DFLT":
            return False
        # explicit control over contested cargo_labels, by specifying which container type should be used (there can only be one type for label based support)
        contested_cargo_labels = {
            "CHLO": "cryo_tank",
            "FOOD": "reefer",
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
                "GestaltGraphicsAutomobilesTransporter.cargo_label_mapping: cargo_label",
                cargo_label,
                "already exists, being over-written by",
                container_type,
                "label",
            )
        # default to allowing, most cargos aren't contested
        return True
    """

    @property
    def cargo_label_mapping(self):
        result = {}
        # see intermodal for example of how this mapped containers
        # for vehicles this maybe just needs to switch e.g on cargo subtype or something - trucks, cars etc
        return result

    @property
    def position_variants(self):
        # used in spriteset templating
        if self.consist_ruleset == "articulated_permanent_twin_sets":
            # permanent articulated twin sets only need 2 variants
            return ["first", "last"]
        elif self.consist_ruleset == "1_unit_sets":
            # 1 unit articulated sets only need 1 variant
            return ["default"]
        elif self.consist_ruleset == "2_unit_sets":
            # 2 unit articulated sets only need 3 variants
            return ["default", "first", "last"]
        else:
            # defaulting to 4 unit sets is apparently fine?
            return ["default", "first", "last", "middle"]

    @property
    def nml_template(self):
        # override in subclasses as needed
        return "vehicle_automobile_car.pynml"


class GestaltGraphicsSimpleBodyColourRemaps(GestaltGraphics):
    """
    Simple recolouring from false body colour to a single default livery
    Recolouring from false body colour makes it easy to adjust base liveries across all vehicles of the same type.
    This gestalt can also be used as a shortcut simply for adding automated chassis.
    """

    def __init__(self, weathered_variants, **kwargs):
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
        # there is no support here for weathered variants that depend on hand-drawn pixels, it's all recolour maps as of March 2022 - could change if needed
        self.weathered_variants = weathered_variants
        self.liveries = kwargs["liveries"]

    @property
    def generic_rows(self):
        utils.echo_message(
            "generic_rows not implemented in GestaltGraphicsSimpleBodyColourRemaps (by design)"
        )
        return None

    @property
    def nml_template(self):
        return "vehicle_with_simple_body_colour_remaps.pynml"

    def get_output_row_types(self):
        return ["simple_recolour_spriterows"]


class GestaltGraphicsConsistPositionDependent(GestaltGraphics):
    """
     Used when the vehicle changes appearance depending on position in the consist
     Intended for pax and mail cars
      - intended for closed vehicles with doors, 'loaded' sprites are same as 'empty'
      - option to show loading sprites (open doors) via 1 or 2 'loading' rows
    - vehicles can be configured to optionally show 1 of 4 different sprites depending on position in consist
         - 'default'
         - 'first'
         - 'last'
         - 'special'
     - 'positions' are flexible, and hax can safely be used within reason to get worthwhile results / save time
         - positions are controlled by consist_rulesets, defined per Consist type as needed
         - the positions are just keywords, mapped onto spriterow nums, and can be remapped fairly freely
     - the limit of 4 is arbitrary, and self-imposed to prevent combinatorial explosion (and consequent need to draw sprites)
    """

    def __init__(self, spriterow_group_mappings, **kwargs):
        super().__init__(**kwargs)
        # spriterow_group_mappings provided by subclass calling gestalt_graphics:
        # - spriterow numbers for named positions in consist
        # - spriterow numbers are zero-indexed *relative* to the start of the consist-cargo block, to reduce shuffling them all if new rows are inserted in future
        # - *all* of the keys must be provided in the mapping, set values to 0 if unused
        self.spriterow_group_mappings = spriterow_group_mappings
        # liveries provided by subclass calling gestalt_graphics
        self.liveries = kwargs.get("liveries", [])
        self.default_livery_extra_docs_examples = kwargs.get(
            "default_livery_extra_docs_examples", []
        )
        # we'll generate spriterows for doors closed and doors open
        self.num_load_state_or_similar_spriterows = 2
        # colour mapping stuff...
        self.colour_mapping_switch = "_switch_colour_mapping"
        self.colour_mapping_switch_purchase = "_switch_colour_mapping"
        self.colour_mapping_with_purchase = True
        # verify that the spriterow_group_mappings keys are in the expected order
        if list(self.spriterow_group_mappings.keys()) != [
            "default",
            "first",
            "last",
            "special",
        ]:
            raise BaseException(
                "Keys aren't correct for spriterow_group_mappings: "
                + str(spriterow_group_mappings)
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
            # note that we simply generate a row per vehicle position variant
            # this method leads to unnecessary rows for many cases
            # but is relied on for multiple unit (railcars etc) where not all vehicles have pans, in which case the row is simply empty
            self.num_pantograph_rows = len(self.liveries) * (
                1 + max(self.spriterow_group_mappings.values())
            )

    @property
    def nml_template(self):
        # override in subclasses as needed
        return "vehicle_consist_position_dependent.pynml"

    def get_output_row_types(self):
        return ["pax_mail_cars_with_doors"]

    @property
    def num_spritesheet_liveries_per_position_variant(self):
        # this counts liveries in the spritesheet, the actual number of liveries may be higher due to sprite reuse with recolouring
        # there is some risk of divergence here from buyable variants, as those aren't passed to gestalt graphics currently
        # buyable variants _could_ be passed, it's just work to get that param added to all the classes using this gestalt
        spriterow_nums_seen = []
        for livery_counter, livery in enumerate(self.liveries):
            if livery.get("relative_spriterow_num", None) is None:
                spriterow_nums_seen.append(livery_counter)
            else:
                spriterow_nums_seen.append(livery["relative_spriterow_num"])
        return len(set(spriterow_nums_seen))

    @property
    def total_spriterow_count(self):
        # n unique liveries * 2 states for doors open/closed * number of position variants defined
        return (
            self.num_spritesheet_liveries_per_position_variant
            * self.num_load_state_or_similar_spriterows
            * self.total_position_variants
        )

    @property
    def total_position_variants(self):
        # rows can be reused across multiple position variant labels, so find uniques
        return len(set(list(self.spriterow_group_mappings.values())))

    @property
    def asymmetric_row_map(self):
        # used in graphics processor to figure out how to make correct asymmetric sprites for 'first' and 'last'
        # pax / mail cars are asymmetric, sprites are drawn in second col, first col needs populated, map is [col 1 dest]: [col 2 source]
        result = {}
        base_row_num = 0
        # This is tied completely to the spritesheet format:
        # [1..4] vehicle variants x n liveries x 2 rows (empty & loaded, loading)
        for position_variant_num in range(self.total_position_variants):
            if position_variant_num == self.spriterow_group_mappings["first"]:
                source_row_num = self.spriterow_group_mappings["last"]
            elif position_variant_num == self.spriterow_group_mappings["last"]:
                source_row_num = self.spriterow_group_mappings["first"]
            else:
                source_row_num = position_variant_num
            # group of n rows - n liveries * two loaded/loading states (opening doors)
            row_group_size = self.num_load_state_or_similar_spriterows * len(
                self.liveries
            )
            for i in range(1, 1 + row_group_size):
                result[base_row_num + (row_group_size * position_variant_num) + i] = (
                    base_row_num + (row_group_size * source_row_num) + i
                )
        return result

    def get_buy_menu_unit_input_row_num(
        self, unit_counter, pipeline, buyable_variant, unit
    ):
        # as of Jan 2024 it was easiest to enforce that this only works with consist comprised of exactly 2 units
        # that means we can just do first / last, and not worry about other position variants
        # support for arbitrary number of units could be added, derived from consist ruleset, but those cases don't exist as of Jan 2024
        if len(pipeline.consist.units) != 2:
            if pipeline.consist.id == "golfinho":
                #JFDI jank
                if unit_counter == 1:
                    position_variant_offset = self.spriterow_group_mappings["special"]
                    unit_variant_row_num = (
                        self.num_spritesheet_liveries_per_position_variant
                        * position_variant_offset
                        * self.num_load_state_or_similar_spriterows
                    ) + (
                        buyable_variant.relative_spriterow_num
                        * self.num_load_state_or_similar_spriterows
                    )
                    return unit_variant_row_num
            else:
                raise BaseException(
                    "GestaltGraphicsConsistPositionDependent.get_buy_menu_unit_input_row_num(): consist "
                    + pipeline.consist.id
                    + " does not have exactly 2 units - this case is not currently supported"
                )

        if unit_counter == 0:
            position_variant_offset = self.spriterow_group_mappings["first"]
        else:
            position_variant_offset = self.spriterow_group_mappings["last"]
        if pipeline.is_pantographs_pipeline:
            unit_variant_row_num = position_variant_offset
        else:
            unit_variant_row_num = (
                self.num_spritesheet_liveries_per_position_variant
                * position_variant_offset
                * self.num_load_state_or_similar_spriterows
            ) + (
                buyable_variant.relative_spriterow_num
                * self.num_load_state_or_similar_spriterows
            )

        return unit_variant_row_num


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
        cargo_row_map=None,
        generic_rows=None,
        unique_spritesets=None,
        cargo_label_mapping=None,
        weathered_variants=None,
        num_extra_layers_for_spritelayer_cargos=None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.pipelines = pipelines.get_pipelines(["pass_through_pipeline"])
        self._nml_template = _nml_template
        self._cargo_row_map = cargo_row_map
        self._generic_rows = generic_rows
        self._unique_spritesets = unique_spritesets
        self._cargo_label_mapping = cargo_label_mapping
        self._weathered_variants = weathered_variants
        self.liveries = kwargs["liveries"]
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

    def get_output_row_types(self):
        return ["custom_cargo"]

    @property
    def cargo_row_map(self):
        return self._cargo_row_map

    @property
    def unique_spritesets(self):
        return self._unique_spritesets

    @property
    def cargo_label_mapping(self):
        return self._cargo_label_mapping

    def buy_menu_row_map(self, pipeline):
        # not implemented as of Jan 2024 - provide custom buy menu sprites via the template and/or manually in the spritesheet
        raise BaseException(
            "buy_menu_row_map called in GestaltGraphicsCustom for consist "
            + pipeline.consist.id
            + " - this isn't supported."
        )

    @property
    def weathered_variants(self):
        if self._weathered_variants == None:
            # provide a default weathered_variant to spriteset templating, iff the template wants this attribute
            return {"unweathered": {}}
        else:
            return self._weathered_variants
