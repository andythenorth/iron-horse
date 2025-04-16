import copy
import importlib
import os
import pickle
import tomllib
from collections import defaultdict, Counter
from functools import cached_property
import time

currentdir = os.curdir

import global_constants
import utils
from utils import timing

# get args passed by makefile
command_line_args = utils.get_command_line_args()

from train.factory import ModelVariantFactory


class Roster:
    """
    Rosters compose a set of vehicles which is complete for gameplay.
    In Iron Horse each roster is compiled to a standalone grf.
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.numeric_id = kwargs.get("numeric_id")
        self.grf_name = kwargs.get("grf_name")
        self.grfid = kwargs.get("grfid")
        self.str_grf_name = kwargs.get("str_grf_name")
        # engine_module_names only used once at __init__ time, it's a list of module names, not the actual model variants
        self.engine_module_names = kwargs.get("engine_module_names")
        self.wagon_module_names_with_roster_ids = kwargs.get(
            "wagon_module_names_with_roster_ids"
        )
        self.engine_model_variants_by_catalogue = defaultdict(list)
        self.wagon_model_variants_by_catalogue = defaultdict(list)
        # create a structure to hold variant groups
        # deliberately instantiated as none - cannot be populated as a structure until later, after all model variants are inited
        self.variant_groups = None
        self.intro_years = kwargs.get("intro_years")
        self.speeds = kwargs.get("speeds")
        self.freight_car_capacity_per_unit_length = kwargs.get(
            "freight_car_capacity_per_unit_length"
        )
        self.pax_car_capacity_per_unit_length = kwargs.get(
            "pax_car_capacity_per_unit_length"
        )
        self.pax_car_capacity_types = kwargs.get("pax_car_capacity_types")
        self.train_car_weight_factors = kwargs.get("train_car_weight_factors")
        self.engine_and_misc_car_liveries = kwargs.get(
            "engine_and_misc_car_liveries", []
        )
        self.pax_mail_livery_groups = kwargs.get("pax_mail_livery_groups", {})
        # tech tree times as fast to create as of April 2025, so no need for conditional creation
        self.engine_model_tech_tree = TechTree.create(roster=self)

    @property
    def model_variants_by_catalogue(self):
        # With unique keys across engine and wagon dictionaries,
        # simply merge them using dictionary unpacking.
        return {
            **self.engine_model_variants_by_catalogue,
            **self.wagon_model_variants_by_catalogue,
        }

    @property
    def engine_catalogues(self):
        return [
            catalogue_entry["catalogue"]
            for catalogue_entry in self.engine_model_variants_by_catalogue.values()
        ]

    @property
    def wagon_catalogues(self):
        return [
            catalogue_entry["catalogue"]
            for catalogue_entry in self.wagon_model_variants_by_catalogue.values()
        ]

    @property
    def catalogues(self):
        # Gather catalogue instances from both engines and wagons
        return self.engine_catalogues + self.wagon_catalogues

    @property
    def engine_model_variants(self):
        # Flatten the list of engine model variants from the nested dict
        return [
            model_variant
            for catalogue_entry in self.engine_model_variants_by_catalogue.values()
            for model_variant in catalogue_entry["model_variants"]
        ]

    @property
    def wagon_model_variants(self):
        # Flatten the list of wagon model variants from the nested dict
        return [
            model_variant
            for catalogue_entry in self.wagon_model_variants_by_catalogue.values()
            for model_variant in catalogue_entry["model_variants"]
        ]

    @property
    def model_variants(self):
        # join both engine and wagon variants
        return self.engine_model_variants + self.wagon_model_variants

    # should be safe to cache this one
    @cached_property
    def wagon_model_variants_by_model_id_root(self):
        result = {}
        for wagon_model_variant in self.wagon_model_variants:
            result.setdefault(wagon_model_variant.model_id_root, [])
            result[wagon_model_variant.model_id_root].append(wagon_model_variant)
        return result

    @property
    def model_variants_in_buy_menu_order(self):
        """
        Returns a flat list of VariantGroup instances, depth-first ordered from the nested parent/child structure.
        """
        result = []

        def walk(group: VariantGroup):
            result.extend(group)
            for child in group.child_groups:
                walk(child)

        for group in self.variant_groups.values():
            if group.parent_group is None:
                walk(group)

        return result

    @property
    def model_variants_in_order_optimised_for_action_2_ids(self):
        # CABBAGE as of April 2025 this produces no improvement in action 2 ID consumption vs. just using model_variants
        # CABBAGE WITHOUT THIS SWITCHES MIGHT NOT BE FOUND FOR RANDOMISED WAGONS
        # the base sort order for model variants is for the buy menu, but this isn't effective for order in nml output
        # because randomised wagons need action 2 IDs spanning multiple other vehicles, and this can cause problems allocating enough action 2 IDs
        # therefore we re-order, to group (as far as we can) vehicles where IDs need to span
        # this isn't infallible, but reduces the extent to which the randomised wagons consume action 2 IDs
        result = []
        randomised_wagons_by_track_gen_length_power = {}

        # Categorize model variants by generation, length, track type, and power
        for model_variant in self.model_variants:
            gen = model_variant.gen
            track_type = model_variant.base_track_type
            power = model_variant.power
            length = model_variant.length

            key = (track_type, gen, length, power)

            if key not in randomised_wagons_by_track_gen_length_power:
                randomised_wagons_by_track_gen_length_power[key] = {
                    "candidates": [],
                    "randomised": [],
                }

            if model_variant.catalogue.model_is_randomised_wagon_type:
                randomised_wagons_by_track_gen_length_power[key]["randomised"].append(
                    model_variant
                )
            else:
                randomised_wagons_by_track_gen_length_power[key]["candidates"].append(
                    model_variant
                )

        # Process each group based on the combined key
        for key in sorted(randomised_wagons_by_track_gen_length_power.keys()):
            candidates = randomised_wagons_by_track_gen_length_power[key]["candidates"]
            randomised_wagons = randomised_wagons_by_track_gen_length_power[key][
                "randomised"
            ]

            # Append candidates first
            result.extend(candidates)

            # Append randomised wagons after their candidates
            result.extend(randomised_wagons)

        return result

    @timing
    def produce_engines(self):
        self.engine_model_variants_by_catalogue = {}
        package_name = "vehicles." + self.id
        roster_id_providing_module = self.id
        for engine_module_name in self.engine_module_names:
            engine_module = importlib.import_module(
                "." + engine_module_name, package_name
            )

            for model_def in engine_module.main():
                factory = ModelVariantFactory(
                    model_def, self.id, roster_id_providing_module
                )
                catalogue = factory.catalogue
                # Use the convenience property `id` on Catalogue
                catalogue_id = catalogue.model_id
                if catalogue_id not in self.engine_model_variants_by_catalogue:
                    self.engine_model_variants_by_catalogue[catalogue_id] = {
                        "catalogue": catalogue,
                        "model_variants": [],
                    }
                for catalogue_entry in catalogue:
                    model_variant = factory.produce(catalogue_entry=catalogue_entry)
                    self.engine_model_variants_by_catalogue[catalogue_id][
                        "model_variants"
                    ].append(model_variant)
                self.engine_model_tech_tree.add_model(catalogue)

    @timing
    def produce_wagons(self):
        # Iterate over wagon module name stems and warn if not in global_constants
        for wagon_module_name_stem in self.wagon_module_names_with_roster_ids.keys():
            if wagon_module_name_stem not in global_constants.wagon_module_name_stems:
                utils.echo_message(
                    f"Warning: ({self.id}) {wagon_module_name_stem} not found in global_constants.wagon_module_name_stems"
                )

        self.wagon_model_variants_by_catalogue = (
            {}
        )  # Reset or initialize the grouping dict

        # temp book-keeping of randomised_wagons
        randomised_wagon_type_catalogues_tmp = []

        for wagon_module_name_stem in global_constants.wagon_module_name_stems:
            if wagon_module_name_stem in self.wagon_module_names_with_roster_ids:
                roster_id_providing_module = self.wagon_module_names_with_roster_ids[
                    wagon_module_name_stem
                ]
                wagon_module_name = (
                    f"{wagon_module_name_stem}_{roster_id_providing_module}"
                )
                package_name = "vehicles." + roster_id_providing_module

                try:
                    wagon_module = importlib.import_module(
                        "." + wagon_module_name, package_name
                    )
                    for model_def in wagon_module.main():
                        factory = ModelVariantFactory(
                            model_def, self.id, roster_id_providing_module
                        )
                        catalogue = factory.catalogue
                        # Using the convenience property 'id'
                        catalogue_id = catalogue.model_id
                        if catalogue_id not in self.wagon_model_variants_by_catalogue:
                            self.wagon_model_variants_by_catalogue[catalogue_id] = {
                                "catalogue": catalogue,
                                "model_variants": [],
                            }
                        for catalogue_entry in catalogue:
                            model_variant = factory.produce(
                                catalogue_entry=catalogue_entry
                            )
                            self.wagon_model_variants_by_catalogue[catalogue_id][
                                "model_variants"
                            ].append(model_variant)
                        if catalogue.model_is_randomised_wagon_type:
                            randomised_wagon_type_catalogues_tmp.append(catalogue)
                except ModuleNotFoundError:
                    raise ModuleNotFoundError(
                        f"{wagon_module_name} in {package_name} as defined by {self.id}.wagon_module_names_with_roster_ids"
                    )
                except Exception:
                    raise
        # we have to provision wagon randomisation candidates after initialising all wagon model variants
        self.cabbage_randomisation_candidates(randomised_wagon_type_catalogues_tmp)

    def cabbage_randomisation_candidates(self, randomised_wagon_type_catalogues_tmp):
        # called by produce_wagons, but separate method so we can isolate and measure timing if we need to

        def get_tmp_uid(model_id_root, catalogue):
            # convenience method for a key, only used for accessing a temp structure
            return f"{model_id_root}_{catalogue.model_def.gen}_{catalogue.base_track_type}_{catalogue.model_def.subtype}"

        cabbage_random_temp_foo = {}
        for catalogue in self.wagon_catalogues:
            for model_id_root in getattr(
                catalogue.factory.model_type_cls, "randomised_candidate_groups", []
            ):
                tmp_uid = get_tmp_uid(model_id_root, catalogue)
                cabbage_random_temp_foo.setdefault(tmp_uid, [])
                cabbage_random_temp_foo[tmp_uid].append(
                    catalogue.example_model_variant
                )

        for catalogue in randomised_wagon_type_catalogues_tmp:
            tmp_uid = get_tmp_uid(
                catalogue.factory.model_type_cls.model_id_root, catalogue
            )
            for model_variant in self.wagon_model_variants_by_catalogue[catalogue.model_id][
                "model_variants"
            ]:
                model_variant.wagon_randomisation_candidates = cabbage_random_temp_foo[
                    tmp_uid
                ]

                if len(model_variant.wagon_randomisation_candidates) == 0:
                    raise BaseException(
                        f"{model_variant.id}"
                        f" did not match any randomisation_candidates, possibly there are no matching wagons for base_id/length/gen"
                    )
                if len(model_variant.wagon_randomisation_candidates) == 1:
                    raise BaseException(
                        f"{model_variant.id}"
                        f" has only one choice for randomisation_candidates\n"
                        f"this will be either a shortage of candidates, or the model should not be declared\n"
                        f"{model_variant.wagon_randomisation_candidates}"
                    )
                if len(model_variant.wagon_randomisation_candidates) > 64:
                    # CABBAGE TEMP
                    model_variant.wagon_randomisation_candidates = (
                        model_variant.wagon_randomisation_candidates[0:8]
                    )
                    continue
                    # we have a limited number of random bits, and we need to use them independently of company colour choices
                    # so guard against consuming too many, 64 variants is 6 bits, and that's all we want to consume
                    raise BaseException(
                        f"{model_variant.id}"
                        f" has more than 64 entries in randomised_candidate_groups, and will run out of random bits; reduce the number of candidates\n"
                        f"{model_variant.wagon_randomisation_candidates}"
                    )

    @property
    def default_livery(self):
        # the default livery if no livery is explicitly specified by name
        return {
            "remap_to_cc": None,
            "docs_image_input_cc": [
                ("COLOUR_BLUE", "COLOUR_BLUE"),
                ("COLOUR_RED", "COLOUR_WHITE"),
            ],
        }

    def get_pax_mail_liveries(self, default_livery_group_name, model_def):
        result = []
        # we can optionally specify liveries per model_variant via the model_def, otherwise use the default for the model type subclass
        if model_def.livery_group_name is not None:
            livery_group_name = model_def.livery_group_name
        else:
            livery_group_name = default_livery_group_name
        # will fail if the livery group is not defined in the roster
        # CABBAGE SHIM
        for livery in self.pax_mail_livery_groups[livery_group_name]:
            livery_result = self.engine_and_misc_car_liveries[livery[0]].copy()
            livery_result["relative_spriterow_num"] = livery[1]
            result.append(livery_result)
        return result

    def intro_year_ranges(self, base_track_type):
        # return a list of year pairs (first year, last year) for generations
        result = []
        end_date = global_constants.max_game_date
        for intro_year in reversed(self.intro_years[base_track_type]):
            result.append((intro_year, end_date))
            end_date = intro_year - 1
        result.reverse()
        return result

    def get_lang_data(self, lang, context):
        # strings optionally vary per roster, so we have a method to fetch all lang data via the roster
        global_pragma = {}
        lang_strings = {}
        # we have the option to suppress selected strings in specific contexts, using a dedicated suppression file
        suppressed_strings = tomllib.load(
            open(
                os.path.join(currentdir, "src", "lang", "suppressed_strings.toml"), "rb"
            )
        )

        with open(os.path.join(currentdir, "src", "lang", lang + ".toml"), "rb") as fp:
            lang_source = tomllib.load(fp)

        for node_name, node_value in lang_source.items():
            # first check if the string is suppressed in this roster, when building grf only (not docs)
            if context == "grf" and node_name in suppressed_strings:
                if self.id in suppressed_strings[node_name].get(
                    "suppressed_rosters", []
                ):
                    continue

            if node_name == "GLOBAL_PRAGMA":
                # explicit handling of global pragma items
                global_pragma["grflangid"] = node_value["grflangid"]
                global_pragma["plural"] = node_value["plural"]
                if node_value.get("gender", False):
                    global_pragma["gender"] = node_value["gender"]
                if node_value.get("case", False):
                    global_pragma["case"] = node_value["case"]
            else:
                # all lang strings should provide a default base value, which can optionally be over-ridden per roster
                if self.id in node_value.keys():
                    lang_strings[node_name] = node_value[self.id]
                else:
                    lang_strings[node_name] = node_value["base"]

        for catalogue in self.catalogues:
            example_model_variant = catalogue.example_model_variant
            if example_model_variant.name is not None:
                lang_strings["STR_NAME_" + example_model_variant.model_id.upper()] = (
                    example_model_variant.name
                )

        return {"global_pragma": global_pragma, "lang_strings": lang_strings}

    @timing
    def validate_vehicle_ids(self, numeric_id_defender):
        # has to be explicitly called after all model variants and units are registered to the roster

        # this structure is used to test for duplicate ids
        model_variant_id_counts = Counter(self.model_variants)

        for model_variant in self.model_variants:
            """
            # pickled test nerfed off as (1) slow (2) mp_logger is now used, which should improve the error output when pickle does fail
            # if model_variant won't pickle, then multiprocessing blows up, catching it here is faster and easier
            try:
                pickle.dumps(model_variant)
            except:
                print("Pickling failed for model_variant:", model_variant.id)
                raise
            """
            if model_variant_id_counts[model_variant.id] > 1:
                raise BaseException(
                    f"Error: vehicle id '{model_variant.id}' is defined more than once - to fix, search src for the duplicate.\n"
                    f"The catalogue for one of them is:"
                    f"{model_variant.catalogue}"
                )
            if len(model_variant.units) == 0:
                raise BaseException(f"Error: {model_variant.id} has no units defined")
            elif len(model_variant.units) == 1:
                if model_variant.base_numeric_id <= global_constants.max_articulated_id:
                    raise BaseException(
                        f"Error: {model_variant.id} with base_numeric_id {model_variant.base_numeric_id} needs a base_numeric_id larger than 16383 "
                        f"as the range below 16383 is reserved for articulated vehicles.\n"
                        f"{model_variant.units}\n"
                        f"Unused IDs might be found in build_logs/id_report.py.log"
                    )
            elif len(model_variant.units) > 1:
                for numeric_id in model_variant.catalogue_entry.unit_numeric_ids:
                    if numeric_id > global_constants.max_articulated_id:
                        raise BaseException(
                            f"Error: {model_variant.id} has a unit variant with numeric_id {numeric_id} which is part of an articulated vehicle "
                            f"and needs a numeric_id smaller than {global_constants.max_articulated_id}.\n"
                            f"Use a lower base_numeric_id in the model_def.\n"
                            f"{model_variant.catalogue.unit_numeric_ids}"
                            f"Unused IDs might be found in build_logs/id_report.py.log"
                        )
            for numeric_id in model_variant.catalogue_entry.unit_numeric_ids:
                if numeric_id in numeric_id_defender:
                    colliding_model_variant = numeric_id_defender[numeric_id]
                    # there is a specific case of reused vehicles that are allowed to overlap IDs (they will be grf-independent, and the compile doesn't actually care)
                    # if model_id_root matches both model variants have been instantiated from the same source module...
                    if hasattr(model_variant, "model_id_root"):
                        if (
                            getattr(colliding_model_variant, "model_id_root", None)
                            == model_variant.model_id_root
                        ):
                            # it's fine if both model variants are then in different rosters, as they will not conflict
                            if (
                                colliding_model_variant.roster.id
                                != model_variant.roster.id
                            ):
                                continue
                    raise ValueError(
                        f"Error: model variant {model_variant.id} has a unit variant with a numeric_id that collides "
                        f"({numeric_id}) with a numeric_id of a unit variant in model variant {colliding_model_variant.id}\n"
                        f"{model_variant.id} {[catalogue_entry.unit_numeric_ids for catalogue_entry in model_variant.catalogue]}\n"
                        f"{colliding_model_variant.id} {[catalogue_entry.unit_numeric_ids for catalogue_entry in colliding_model_variant.catalogue]}\n"
                        f"Unused IDs might be found in build_logs/id_report.py.log"
                    )
                else:
                    numeric_id_defender[numeric_id] = model_variant
        # no return value needed

    def add_variant_groups(self):
        # creating groups has to happen after *all* model variants are inited

        # create the structure to hold the groups, this is set to None when the roster is inited, and should be None when this method is called
        if self.variant_groups is not None:
            raise BaseException(
                "add_variant_groups() called more than once for roster " + self.id
            )

        self.variant_groups = {}

        # for every buyable variant for every model_variant
        # - add a group if it doesn't already exist
        # - add the buyable variant as a member of the group
        for model_variant in self.model_variants:
            variant_group_id = model_variant.catalogue_entry.variant_group_id
            if variant_group_id is None:
                raise ValueError(model_variant.id)
            variant_group = self.variant_groups.setdefault(
                variant_group_id, VariantGroup(id=variant_group_id)
            )
            variant_group.append(model_variant)

        # handle nesting of static and random wagon groups
        # logic: if both a `_static` and `_random` group exist for the same base ID,
        #        then the static group is nested into the random group
        for variant_group_id, variant_group in self.variant_groups.items():
            if not variant_group_id.endswith("_static"):
                continue

            # derive the base ID stem (everything before `_static`)
            group_id_stem = variant_group_id.rsplit("_static", 1)[0]
            random_group_id = f"{group_id_stem}_random"
            random_group = self.variant_groups.get(random_group_id)

            if random_group and len(random_group) > 0:
                variant_group.parent_group = random_group
                random_group.child_groups.append(variant_group)


class VariantGroup(list):
    """
    Simple class to manage providing the variant_group nml property.
    List members are model_variant instances.
    Extends default python list, as it's a convenient behaviour (the instantiated class instance behaves like a list object).
    """

    def __init__(self, id):
        self.id = id
        self.parent_group = None
        self.child_groups = []

    def get_variant_group_prop_for_model_variant(self, model_variant):
        # faff to find the group leader (typically the first variant)
        leader = self[0]
        if self.parent_group is not None:
            if model_variant == self[0] or self.flatten_short_group:
                leader = self.parent_group[0]

        # guard - don't assign a group reference to the leader itself
        if leader == model_variant:
            return None

        # for nml, we want the id of the first unit
        return leader.units[0].id

    @property
    def flatten_short_group(self):
        # don't bother nesting short groups
        return len(self) < 3

    @cached_property
    def group_level(self):
        level = 0
        context = self
        while context.parent_group is not None:
            level += 1
            context = context.parent_group
        return level


class TechTree(dict):
    """
    Dedicated class to handle tech trees.
    Intended to be singleton per roster.
    Dict, keyed on base_track_type.
    """


    # to avoid having a very complicated __init__ against (dict) we faff around with this class method, GPT reports that it's idiomatic, I _mostly_ agree
    @classmethod
    def create(cls, *, roster=None):
        instance = cls()
        instance.roster = roster
        # minor optimisation, this avoids repeatedly walking catalogues for the niche case of explicit replacement_model_id
        instance.explicit_replacements_cached = {}
        return instance

    def add_model(self, catalogue):
        if catalogue.clone_quacker.quack:
            # clones don't get added to the tree
            return

        track_type = catalogue.base_track_type
        role = catalogue.example_model_variant.role
        subrole = catalogue.example_model_variant.subrole
        subrole_child_branch_num = (
            catalogue.example_model_variant.subrole_child_branch_num
        )

        role_dict = self._ensure_role_dict(track_type, role)
        subrole_dict = self._ensure_subrole_dict(role_dict, subrole)
        branch_dict = self._ensure_branch_dict(
            subrole_dict, subrole_child_branch_num, track_type=track_type
        )
        branch_dict[catalogue.model_def.gen] = catalogue

        # mild optimisation of lookups for explicit manual replacement of catalogues
        if catalogue.model_def.replacement_model_id is not None:
            self.explicit_replacements_cached.setdefault(catalogue.model_def.replacement_model_id, []).append(catalogue)

    def _ensure_role_dict(self, track_type, role):
        if track_type not in self:
            self[track_type] = {}
        if role not in self[track_type]:
            self[track_type][role] = {}
        return self[track_type][role]

    def _ensure_subrole_dict(self, role_dict, subrole):
        if subrole not in role_dict:
            role_dict[subrole] = {}
        return role_dict[subrole]

    def _ensure_branch_dict(
        self, subrole_dict, subrole_child_branch_num, *, track_type
    ):
        if subrole_child_branch_num not in subrole_dict:
            gens = self._valid_gens_for_track_type(track_type)
            subrole_dict[subrole_child_branch_num] = {gen: None for gen in gens}
        return subrole_dict[subrole_child_branch_num]

    def _valid_gens_for_track_type(self, track_type: str) -> list[int]:
        if not self.roster or not hasattr(self.roster, "intro_years"):
            raise RuntimeError(
                "TechTree requires a roster with intro_years to infer valid generations."
            )
        years = self.roster.intro_years.get(track_type)
        if not years:
            raise ValueError(f"No intro years defined for track type: {track_type}")
        return [i + 1 for i in range(len(years))]

    def _get_branch_for_catalogue(self, catalogue):
        example_model_variant = catalogue.example_model_variant
        # Attempt to access the branch for this catalogue.
        try:
            branch = self[catalogue.base_track_type][example_model_variant.role][
                example_model_variant.subrole
            ][example_model_variant.subrole_child_branch_num]
        except KeyError as e:
            raise KeyError(
                f"Error accessing branch for catalogue {catalogue.model_id}: {e}"
            ) from e
        return branch

    def get_relative_catalogue(self, catalogue, offset: int):
        target_branch = self._get_branch_for_catalogue(catalogue)
        target_gen = catalogue.model_def.gen + offset

        # Branch keys are pre-provisioned with valid gens (1,2,...,max).
        # If target_gen is below 1 or above the highest valid generation,
        # then this catalogue is at the start or end of its branch: return None.
        if target_gen < 1 or target_gen > max(target_branch):
            return None

        # Otherwise, if the key exists in the branch, return its value
        # (even if that value is None, which is acceptable).
        if target_gen in target_branch:
            return target_branch[target_gen]
        else:
            # This case should not occur given our pre-provisioning.
            raise KeyError(
                f"Target generation {target_gen} missing in target_branch for catalogue {catalogue.model_id}"
            )

    def get_next_gen_catalogue(self, catalogue):
        # find the catalogue a catalogue is replaced by in the next generation, if any
        # catalogues (model) have exactly 1 replacement catalogue (model) or None

        # clones don't get added to the tree, so we swap the catalogue if it's a clone
        catalogue = catalogue.clone_quacker.resolve_catalogue(permissive=True)

        # this method might not work for wagons, callers should guard against calling in that case
        if catalogue.model_def.replacement_model_id is not None:
            # ocasionally we need to merge two branches of the subrole, in this case set replacement_model_id on the model_def
            return self.roster.model_variants_by_catalogue[
                catalogue.model_def.replacement_model_id
            ]["catalogue"]

        # models can span generations, so walk forward to find if there's a replacement in the line
        max_gen = max(
            self._valid_gens_for_track_type(
                catalogue.base_track_type
            )
        )
        offset = 1
        while (catalogue.model_def.gen + offset) <= max_gen:
            candidate_catalogue = self.get_relative_catalogue(catalogue, offset)
            if candidate_catalogue is not None:
                return candidate_catalogue
            offset += 1
        # fall through to None
        return None

    def get_previous_gen_catalogues(self, catalogue):
        # find the catalogues a catalogue replaces in the previous generation, if any
        # a catalogue (model) can replace multiple catalogues (models) or None

        # clones don't get added to the tree, so we swap the catalogue if it's a clone
        catalogue = catalogue.clone_quacker.resolve_catalogue(permissive=True)

        result = []

        # first check same line...
        # ...models can span generations, so walk back to find if there's a replacement
        min_gen = 1
        offset = -1
        while (catalogue.model_def.gen + offset) >= min_gen:
            candidate_catalogue = self.get_relative_catalogue(catalogue, offset)
            if candidate_catalogue is not None:
                # stop checking same line if candidate found is found
                result.append(candidate_catalogue)
                break
            offset -= 1

        # handle any manually defined explicit replacements of other catalogues
        result.extend(self.explicit_replacements_cached.get(catalogue.model_id, []))

        return result

    def get_similar_model_catalogues(self, catalogue, power_tolerance_pct=0.4):
        """
        Return catalogues similar to the given one, scoped to same track_type, role,
        subrole, and generation. Also considers adjacent generations:
        - If this catalogue has no next-gen replacement, look at next gen.
        - Always look at previous gen catalogues with no replacement.
        - Freight engines may also consider express engines (but not vice versa).
        """
        # clones don't get added to the tree, so we swap the catalogue if it's a clone
        catalogue = catalogue.clone_quacker.resolve_catalogue(permissive=True)

        base_track_type = catalogue.base_track_type
        role = catalogue.example_model_variant.role
        gen = catalogue.model_def.gen
        target_power = getattr(catalogue.example_model_variant, "power", None)

        # Determine which roles to include in the search
        roles_to_check = [role]
        if role == "freight":
            roles_to_check.append("express")

        # Reverse map: subrole → role
        subrole_to_role = {
            sub: r
            for r, subroles in global_constants.role_subrole_mapping.items()
            for sub in subroles
        }

        # Collect all relevant branch dicts
        branch_dicts = []
        for r in roles_to_check:
            for subrole_key in global_constants.role_subrole_mapping.get(r, []):
                candidate_role = subrole_to_role.get(subrole_key)
                if candidate_role is None:
                    continue
                try:
                    branches = self[base_track_type][candidate_role][subrole_key]
                    branch_dicts.extend(branches.values())  # <- pull each individual branch
                except KeyError:
                    continue

        def is_similar_candidate(candidate):
            if not candidate or candidate is catalogue:
                return False
            if candidate.clone_quacker.quack:
                return False
            if target_power is not None:
                candidate_power = getattr(candidate.example_model_variant, "power", None)
                if candidate_power is not None:
                    lower = target_power * (1 - power_tolerance_pct)
                    upper = target_power * (1 + power_tolerance_pct)
                    if not (lower <= candidate_power <= upper):
                        return False
            return True

        results = []

        # Same generation
        for branch in branch_dicts:
            candidate = branch.get(gen)
            if is_similar_candidate(candidate):
                results.append(candidate)

        # Next gen fallback if no explicit replacement
        if self.get_next_gen_catalogue(catalogue) is None:
            for branch in branch_dicts:
                candidate = branch.get(gen + 1)
                if is_similar_candidate(candidate):
                    results.append(candidate)

        # Previous gen candidates with no replacement
        for branch in branch_dicts:
            candidate = branch.get(gen - 1)
            if is_similar_candidate(candidate):
                if self.get_next_gen_catalogue(candidate) is None:
                    results.append(candidate)

        if len(results) == 0:
            print(catalogue.model_id, " has no similar catalogues")

        return results

    @cached_property
    def simplified_tree(self) -> dict:
        """
        Return a simplified version of the TechTree in which any branch where
        subrole_child_branch_num is negative is dropped. Additionally, any roles
        or subrole entries that become empty after the prune are removed.

        The returned dict has the same general structure as the TechTree:
            { track_type: { role: { subrole: { subrole_child_branch_num: { gen: catalogue, ... } } } } }
        but with branches (keys) < 0 removed.
        """
        simplified = {}
        for track_type, roles in self.items():
            new_roles = {}
            for role, subroles in roles.items():
                new_subroles = {}
                for subrole, branches in subroles.items():
                    # Drop branches with subrole_child_branch_num < 0.
                    new_branches = {branch: branch_dict
                                    for branch, branch_dict in branches.items()
                                    if branch >= 0}
                    # Only add this subrole if there's at least one valid branch.
                    if new_branches:
                        new_subroles[subrole] = new_branches
                # Only add the role if there's at least one valid subrole.
                if new_subroles:
                    new_roles[role] = new_subroles
            # Only add the track_type if there's at least one valid role.
            if new_roles:
                simplified[track_type] = new_roles
        return simplified
