import polar_fox
import gestalt_graphics.graphics_constants as graphics_constants
from gestalt_graphics import pipelines
import utils
import global_constants


class GestaltGraphics(object):
    """
    Simple class, which is extended in sub-classes to configure:
     - base vehicle recolour (if any)
     - cargo graphics (if any)
     - pantographs (if any)
     - other processing as required
    """

    def __init__(self):
        # by default, pipelines are empty
        self.pipelines = pipelines.get_pipelines([])
        # this is only used by engines as of Dec 2022, but we provide a default value here to avoid requiring getattr() in many places, which was masking errors
        self.alternative_liveries = []  # over-ride as needed in subclasses
        # sometimes processing may depend on another generated vehicle spritesheet, so there are multiple processing priorities, 1 = highest
        self.processing_priority = 1
        # default value for optional mask layer, this is JFDI for 2022, may need converting a more generic spritelayers structure in future
        # set directly by the consist self.gestalt_graphics.add_masked_overlay = True, or by kwargs on a specific gestalt subclass
        self.add_masked_overlay = False
        self.buy_menu_width_addition = 0

    @property
    def nml_template(self):
        # over-ride in sub-classes as needed
        # return a pnml file name, e.g. `return 'vehicle_default.pynml'`
        return None

    @property
    def num_cargo_sprite_variants(self):
        # this tends to be common across multiple templates, so provide it in the base class
        # rows can be reused across multiple cargo labels, so find uniques (assumes row nums are identical when reused across labels)
        # !! fails if the subclass doesn't have cargo_row_map
        row_nums_seen = []
        for row_nums in self.cargo_row_map.values():
            for row_num in row_nums:
                row_nums_seen.append(row_num)
        return len(set(row_nums_seen))

    def get_output_row_types(self):
        # stub, for compatibility reasons
        return ["single_row"]

    @property
    def all_liveries(self):
        # a convenience property to insert a default_livery for ease of constructing template repeats
        # note that default_livery is not guaranteed to contain all the key/value pairs that alternative_liveries has
        result = []
        default_livery = {}
        result.append(default_livery)
        result.extend(self.alternative_liveries)
        return result


class GestaltGraphicsEngine(GestaltGraphics):
    """
    Simple Gestalt specifically for engines that have absolutely no other graphics processing except pantograph generation.
    Any Gestalt can also add pantographs as needed (it's a method on Pipeline base class).
    """

    def __init__(self, **kwargs):
        super().__init__()
        self.pipelines = pipelines.get_pipelines(["check_buy_menu_only"])
        self.colour_mapping_switch = "_switch_colour_mapping"
        self.colour_mapping_with_purchase = True
        self.alternative_liveries = kwargs["alternative_liveries"]
        self.default_livery_extra_docs_examples = kwargs.get(
            "default_livery_extra_docs_examples", []
        )
        if kwargs.get("pantograph_type", None) is not None:
            self.pipelines.extend(
                pipelines.get_pipelines(
                    [
                        "generate_pantographs_up_spritesheet",
                        "generate_pantographs_down_spritesheet",
                    ]
                )
            )

    @property
    def nml_template(self):
        return "vehicle_engine.pynml"

    # get_output_row_types not re-implemented here as of July 2020, as no actual pixa processing is used for the engine sprites, add it if processing is needed in future

class GestaltGraphicsOnlyAddPantographs(GestaltGraphics):
    """
    Simple Gestalt specifically for engines that have absolutely no other graphics processing except pantograph generation.
    Any Gestalt can also add pantographs as needed (it's a method on Pipeline base class).
    Unused as of July 2020 as replaced by GestaltGraphicsEngine
    """

    def __init__(self):
        # super appears to not be used, that may or may not be intentional, I didn't change it as of July 2020 as it risks introducing unexpected results
        # no graphics processing by default
        self.pipelines = pipelines.get_pipelines(
            [
                "check_buy_menu_only",
                "generate_pantographs_up_spritesheet",
                "generate_pantographs_down_spritesheet",
            ]
        )


class GestaltGraphicsRandomisedWagon(GestaltGraphics):
    """
    Simple Gestalt specifically for randomised wagons that have borrow sprites from other vehicles.
    """

    def __init__(self, **kwargs):
        super().__init__()
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
        # randomised buy menu sprites depend on generated vehicle spritesheet, so defer processing to round 2
        self.processing_priority = 2

    @property
    def nml_template(self):
        return "vehicle_randomised.pynml"

    def buy_menu_sprite_variants(self, consist):
        # note that for randomised wagons, the list of candidates is compile time non-deterministic
        # so the resulting sprites may vary between compiles - this is accepted as of August 2022
        source_data = [
            # vehicle id, y offset to buy menu row
            (
                list(
                    set(consist.frozen_roster_items["wagon_randomisation_candidates"])
                )[0],
                0,
            ),
            (
                list(
                    set(consist.frozen_roster_items["wagon_randomisation_candidates"])
                )[1],
                0,
            ),
        ]
        # buy menu sprite generation supports providing multiple variants (used for cabooses)
        # but here we only need one, in the default buy menu position
        return {0: source_data}


class GestaltGraphicsVisibleCargo(GestaltGraphics):
    """
    Used for vehicle with visible cargos
    Supports *only* pixa-generated cargos; mixing with custom cargo rows isn't handled, TMWFTLB
    Should not be used with 'random_reverse' property, composited cargos are symmetric, so cargo template doesn't handle random_reverse.
    """

    def __init__(self, **kwargs):
        super().__init__()
        self.pipelines = pipelines.get_pipelines(
            ["extend_spriterows_for_composited_sprites_pipeline"]
        )
        # default unweathered body recolour to CC1, pass param to over-ride as needed
        # can optionally extend with "weathered" variant and an appropriate recolour map
        # (weathered variant only used for non-CC body recolouring; CC will provide variants via recolour sprites automatically)
        self.weathered_variants = kwargs.get(
            "weathered_variants", {"unweathered": graphics_constants.body_recolour_CC1}
        )
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

        for flipped in ["unflipped", "flipped"]:
            start_y_cumulative = graphics_constants.spritesheet_top_margin

            if self.has_cover:
                # add rows for covered sprite
                for weathered_variant in self.weathered_variants.keys():
                    result.append(
                        ["has_cover_" + weathered_variant, flipped, start_y_cumulative]
                    )
                    start_y_cumulative += row_height

            # add rows for empty sprite
            for weathered_variant in self.weathered_variants.keys():
                result.append(
                    ["empty_" + weathered_variant, flipped, start_y_cumulative]
                )
                start_y_cumulative += row_height

            # !! not sure unique_cargo_rows order will always reliably match to what's needed, but if it doesn't, explicitly sort it eh
            for row_num in unique_cargo_rows:
                result.append(
                    [
                        "loading_" + str(row_num),
                        flipped,
                        start_y_cumulative,
                    ]
                )
                result.append(
                    [
                        "loaded_" + str(row_num),
                        flipped,
                        start_y_cumulative + 30,
                    ]
                )
                start_y_cumulative += 2 * row_height
        return result


class GestaltGraphicsBoxCarOpeningDoors(GestaltGraphics):
    """
    Used to handle the specific case of box-type freight cars
    - can handle id_base to produce multiple types of vehicle from one input template
    - doors open during loading
    - no cargo is shown by design (TMWFTLB: piece sprites could be generated in, but setting up masks etc for all vehicles is unwanted complexity)
    """

    def __init__(self, weathered_variants, **kwargs):
        super().__init__()
        # as of Jan 2018 only one pipeline is used, but support is in place for alternative pipelines
        self.pipelines = pipelines.get_pipelines(
            ["extend_spriterows_for_composited_sprites_pipeline"]
        )
        self.id_base = kwargs.get("id_base")
        # a default 'unweathered' variant must be provided
        # additional sets of recolour maps can be provided to generate 'weathered' sprites
        # these will be randomly selected in-game for visual variety
        # this is separate and complementary to the minor variations to vehicle company colours using in-game recolour sprites
        # there is no support here for weathered variants that depend on hand-drawn pixels, it's all recolour maps as of March 2022 - could change if needed
        # note also that box cars have only one recolour map for *cargo*, which should be on 'DFLT',
        self.weathered_variants = weathered_variants

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
        super().__init__()
        # as of Jan 2018 only one pipeline is used, but support is in place for alternative pipelines
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

    def buy_menu_sprite_variants(self, consist):
        result = {}
        for counter, buy_menu_sprite_pair in enumerate(self.buy_menu_sprite_pairs):
            # vehicle id, y offset to buy menu row
            source_data = [
                (
                    consist,
                    self.spriterow_labels.index(buy_menu_sprite_pair[0]),
                ),
                (
                    consist,
                    self.spriterow_labels.index(buy_menu_sprite_pair[1]),
                ),
            ]

            result[counter] = source_data
        return result


class GestaltGraphicsIntermodalContainerTransporters(GestaltGraphics):
    """
    Dedicated gestalt for intermodal container transporter
    Gestalt handles both
    - the consist sprites
    - the spritelayer cargos which are in separate layer
    """

    def __init__(self, **kwargs):
        super().__init__()
        # we use the composited sprites pipeline so we can make use of chassis compositing
        self.pipelines = pipelines.get_pipelines(
            ["extend_spriterows_for_composited_sprites_pipeline"]
        )
        # we need to run the spritelayer cargo pipelines separately from the vehicle pipelines, but we still use this gestalt as the entry point
        self.spritelayer_cargo_pipelines = pipelines.get_pipelines(
            ["generate_spritelayer_cargo_sets"]
        )
        self.colour_mapping_switch = "_switch_colour_mapping"
        self.colour_mapping_with_purchase = False
        self.consist_ruleset = kwargs.get("consist_ruleset", None)
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
                "label",
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

            # then insert or over-ride entries with cargo_label: (container_type, [CARGO_LABEL]) where there are explicit graphics for a cargo
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
        # over-ride in sub-classes as needed
        return "vehicle_intermodal.pynml"


class GestaltGraphicsAutomobilesTransporter(GestaltGraphics):
    """
    Dedicated automobiles (car, truck, tractor) transporter
    Gestalt handles both
    - the consist sprites
    - the spritelayer cargos which are in separate layer
    """

    def __init__(self, spritelayer_cargo_layers=["default"], **kwargs):
        super().__init__()
        # we use the composited sprites pipeline so we can make use of chassis compositing
        self.pipelines = pipelines.get_pipelines(
            ["extend_spriterows_for_composited_sprites_pipeline"]
        )
        # we need to run the spritelayer cargo pipelines separately from the vehicle pipelines, but we still use this gestalt as the entry point
        self.spritelayer_cargo_pipelines = pipelines.get_pipelines(
            ["generate_spritelayer_cargo_sets"]
        )
        self.colour_mapping_switch = "_switch_colour_mapping"
        self.colour_mapping_with_purchase = False
        self.consist_ruleset = kwargs.get("consist_ruleset", None)
        self.cargo_sprites_are_asymmetric = True
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
                consist_ruleset
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
        for flipped in ["unflipped", "flipped"]:
            start_y_cumulative = graphics_constants.spritesheet_top_margin

            # add rows for empty sprite
            for variant in self.position_variants:
                for vehicle_spritelayer_name in self.vehicle_spritelayer_names:
                    result.append(
                        [
                            vehicle_spritelayer_name + "_" + variant,
                            flipped,
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
        # over-ride in sub-classes as needed
        return "vehicle_automobile_car.pynml"


class GestaltGraphicsSimpleBodyColourRemaps(GestaltGraphics):
    """
    Simple recolouring from false body colour to:
    - a single default livery
    - optional extra liveries for specific cargos

    Recolouring from false body colour makes it easy to adjust liveries across all vehicles of the same type.
    This gestalt can also be used as a shortcut simply for adding automated chassis.
    """

    def __init__(self, weathered_variants, **kwargs):
        super().__init__()
        # as of Jan 2018 only one pipeline is used, but support is in place for alternative pipelines
        self.pipelines = pipelines.get_pipelines(
            ["extend_spriterows_for_composited_sprites_pipeline"]
        )
        # recolour_maps map cargo labels to liveries, use 'DFLT' as the labe in the case of just one livery
        # a default 'unweathered' variant must be provided
        # additional sets of recolour maps can be provided to generate 'weathered' sprites
        # if cargo recolours are provided weathered and unweathered MUST provide the same cargo support
        # these will be randomly selected in-game for visual variety
        # this is separate and complementary to the minor variations to vehicle company colours using in-game recolour sprites
        # there is no support here for weathered variants that depend on hand-drawn pixels, it's all recolour maps as of March 2022 - could change if needed
        self.weathered_variants = weathered_variants

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
        return ["livery_spriterows"]

    @property
    def cargo_row_map(self):
        result = {}
        counter = 0
        # take the cargo recolour maps for 'unweathered' as the default
        for cargo_map in self.weathered_variants["unweathered"]:
            result[cargo_map[0]] = [
                counter
            ]  # list with a single value, as cargo labels can map to multiple rows, but no plan to use that for this gestalt (June 2020)
            counter += 1
        return result


class GestaltGraphicsConsistSpecificLivery(GestaltGraphics):
    """
     Used when the vehicle changes livery to match
     - the engine (based on engine 'role')
     - major cargo refit in the consist (mail vs. freight)
     - position in consist (pax restaurant cars etc)
     Intended for pax and mail cars
      - multiple engine roles might map to one livery
      - livery shown is specific to the engine role and/or the major cargo in the consist
      - player can toggle engine-livery or solid CC by flipping vehicle
      - intended for closed vehicles with doors, 'loaded' sprites are same as 'empty'
      - option to show cargo loading sprites (open doors) via 1 or 2 'loading' rows
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
        # no graphics processing for this gestalt
        super().__init__()
        # spriterow_group_mappings provided by subclass calling gestalt_graphics:
        # (1) consist-cargo types for which specific liveries are provided
        # (2) spriterow numbers for named positions in consist
        # spriterow numbers are zero-indexed *relative* to the start of the consist-cargo block, to reduce shuffling them all if new rows are inserted in future
        # *all* of the values in consist_positions_ordered must be provided in the mapping, set them to 0 if unused
        self.spriterow_group_mappings = spriterow_group_mappings
        self.colour_mapping_switch = "_switch_colour_mapping"
        self.colour_mapping_with_purchase = False
        # rulesets are used to define for different types of vehicle how sprites change depending on consist position
        self.consist_ruleset = kwargs.get("consist_ruleset", None)
        # it's nice to use a dict for the consist position->row mapping, but order matters for the spritesheet, so have an ordered set of keys
        # also, although rulesets allow fine-grained control, there are deliberately only 4 configuration options
        # this stops rules getting out of control and simplifies other methods
        self.consist_positions_ordered = ["default", "first", "last", "special"]

        self.pipelines = pipelines.get_pipelines(
            ["extend_spriterows_for_composited_sprites_pipeline"]
        )
        if kwargs.get("pantograph_type", None) is not None:
            self.pipelines.extend(
                pipelines.get_pipelines(
                    [
                        "generate_pantographs_up_spritesheet",
                        "generate_pantographs_down_spritesheet",
                    ]
                )
            )
            # this relies on DFLT mapping being safe to take
            # *and* assumes no gaps in the spriterows, so take the max spriterow num
            # *and* assumes 2 liveries are in use
            # note the +1 because livery rows are zero indexed
            self.num_pantograph_rows = 2 * (
                max([int(i) + 1 for i in self.cargo_row_map["DFLT"]])
            )

    @property
    def nml_template(self):
        # over-ride in sub-classes as needed
        return "vehicle_with_consist_specific_liveries.pynml"

    def get_output_row_types(self):
        return ["pax_mail_cars_with_doors"]

    def get_position_variants_with_keys(self, cargo_row_map):
        # just formatting for human-readable access to positions in templates where mapping[0][n] was fiddly
        # the cargo_row_map structure can't use a dict for compatibility reasons, so handle it here
        result = {}
        for i, name in enumerate(self.consist_positions_ordered):
            result[name] = cargo_row_map[1][i]
        return result

    @property
    def cargo_row_map(self):
        # This is tied completely to the spritesheet format, which as of April 2018 was:
        # - pax consist liveries (n vehicle variants x 2 liveries x 2 rows: empty & loaded, loading)
        # - mail consist liveries (n vehicle variants x 2 liveries x 2 rows: empty & loaded, loading)
        # these are mapped by the subclass using spriterow_group_mappings to consist positions that
        #   the template expects for e.g. restaurant cars, brake coaches etc
        result = {}
        counter = 0
        # this doesn't account for cargos like TOUR, but could be extended so cargo labels are a list, TMWFTLB as of April 2018 though
        # not a dict because order matters
        for livery_type, cargo_label in (("pax", "PASS"), ("mail", "MAIL")):
            if livery_type in self.spriterow_group_mappings:
                # we have to rebuild the row_nums in a predictable order (they're stored in a dict for convenience when configuring)
                relative_row_nums = [
                    self.spriterow_group_mappings[livery_type][position]
                    for position in self.consist_positions_ordered
                ]
                result[cargo_label] = [
                    counter + row_num for row_num in relative_row_nums
                ]  # we make relative row_nums absolute here
                counter += len(set(relative_row_nums))
        # we rely on DFLT here to explicitly catch the case for 'freight' (which has no label we can check)
        if "DFLT" not in result.keys():
            # this will error if neither pax nor mail are defined
            # default to mail if available (to handle mail cars in freight consists)
            if "MAIL" in result.keys():
                result["DFLT"] = result["MAIL"]
            else:
                # fallback to pax if nothing else
                result["DFLT"] = result["PASS"]
        return result

    @property
    def asymmetric_row_map(self):
        # used in graphics processor to figure out how to make correct asymmetric sprites for 'first' and 'last'
        # pax / mail cars are asymmetric, sprites are drawn in second col, first col needs populated, map is [col 1 dest]: [col 2 source]
        result = {}
        base_row_num = 0
        # This is tied completely to the spritesheet format, which as of April 2018 was:
        # - pax consist liveries (n vehicle variants x 2 liveries x 2 rows: empty & loaded, loading)
        # - mail consist liveries (n vehicle variants x 2 liveries x 2 rows: empty & loaded, loading)
        # see also cargo_row_map()
        for livery_type, cargo_label in (("pax", "PASS"), ("mail", "MAIL")):
            if livery_type in self.spriterow_group_mappings:
                spriterow_group_mapping = self.spriterow_group_mappings[livery_type]
                num_rows = len(set(spriterow_group_mapping.values()))

                for variant_num in range(num_rows):
                    if variant_num == spriterow_group_mapping["first"]:
                        source_row_num = spriterow_group_mapping["last"]
                    elif variant_num == spriterow_group_mapping["last"]:
                        source_row_num = spriterow_group_mapping["first"]
                    else:
                        source_row_num = variant_num
                    # group of 4 rows - two liveries * two loaded/loading states (opening doors)
                    for i in range(1, 5):
                        result[base_row_num + (4 * variant_num) + i] = (
                            base_row_num + (4 * source_row_num) + i
                        )
                base_row_num += 4 * num_rows
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
        cargo_row_map=None,
        generic_rows=None,
        unique_spritesets=None,
        cargo_label_mapping=None,
        weathered_variants=None,
        num_extra_layers_for_spritelayer_cargos=None,
    ):
        super().__init__()
        self.pipelines = pipelines.get_pipelines(["pass_through_pipeline"])
        self._nml_template = _nml_template
        self._cargo_row_map = cargo_row_map
        self._generic_rows = generic_rows
        self._unique_spritesets = unique_spritesets
        self._cargo_label_mapping = cargo_label_mapping
        self._weathered_variants = weathered_variants
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

    @property
    def weathered_variants(self):
        if self._weathered_variants == None:
            # provide a default weathered_variant to spriteset templating, iff the template wants this attribute
            return {"unweathered": {}}
        else:
            return self._weathered_variants
