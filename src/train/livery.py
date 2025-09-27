from dataclasses import dataclass, field, replace
from typing import Any, Dict, List, Optional
from itertools import cycle, islice
from functools import cached_property

import global_constants


@dataclass
class LiveryDef:
    livery_name: str
    # alphabetised optional attrs
    colour_set_names: List = field(default_factory=list)
    docs_image_input_cc: Optional[List] = None
    is_freight_wagon_livery: Optional[bool] = False
    purchase_swatch_colour_set_names: List = field(default_factory=list)
    proxy_livery_for_badge_display_and_filter: Optional[str] = None
    relative_spriterow_num: Optional[int] = None
    remap_to_cc: Optional[str] = None
    use_weathering: Optional[bool] = False

    @property
    def purchase_swatch(self):
        if not self.is_freight_wagon_livery:
            return None
        # for any case where we want to control swatches, use purchase_swatch_colour_set_names
        if len(self.purchase_swatch_colour_set_names) > 0:
            return self.purchase_swatch_colour_set_names
        # default to colour_set_names, but we only want uniques
        return list(set(self.colour_set_names))

    @property
    def display_and_filter_name_badge_label(self):
        # conforms to draft livery spec in grf docs as of Apr 2025
        if self.is_freight_wagon_livery:
            subcategory = "freight_wagon/"
        else:
            subcategory = ""
        if self.proxy_livery_for_badge_display_and_filter is not None:
            livery_name = self.proxy_livery_for_badge_display_and_filter
        else:
            livery_name = self.livery_name
        return f"livery/iron_horse/{subcategory}{livery_name.lower()}"

    @property
    def internal_name_badge_label(self):
        # conforms to draft livery spec in grf docs as of Apr 2025
        if self.is_freight_wagon_livery:
            subcategory = "freight_wagon/"
        else:
            subcategory = ""
        return f"ih_livery_def/internal_livery_name/{self.livery_name.lower()}"

    @property
    def weathering_badge_label(self):
        return f"ih_livery_def/use_weathering/{self.use_weathering}"


class LiverySupplier(dict):
    """
    A lightweight supplier of canonical LiveryDef instances.

    This class stores LiveryDef instances keyed by their immutable livery names.
    It allows efficient lookup and delivers modified copies of these instances on demand.
    Intended for use as a singleton in contexts such as templates or compile-time operations.
    """

    def __init__(self):
        self.delivered_liveries = []

    def add_livery(self, livery_name: str, **kwargs):
        livery = LiveryDef(livery_name, **kwargs)
        # all freight wagons use weathering by default
        if livery.is_freight_wagon_livery:
            livery.use_weathering = True
        # liveries can be defined in multiple rosters, for simplicity, if they're exact duplicates we allow that
        # otherwise the liveries need de-duplicated by changing one of their names
        if livery_name in self:
            if self[livery_name].__dict__ != livery.__dict__:
                raise ValueError(
                    f"LiverySupplier.add_livery: a roster tried to change the values for {livery_name}, which has already been defined.\n"
                    f"Liveries with the same name can be added by multiple rosters, but only if they have identical values."
                )
        self[livery_name] = livery
        # no return as of now, not needed

    def deliver(self, livery_name: str, relative_spriterow_num: int):
        # Return a modified copy of the canonical LiveryDef identified by livery_name.

        # regrettable special case handling of detecting weathering, as we want to use only simple constants to fetch liveries
        # we weather all liveries by default, and use livery_name sufix to specify when to not weather
        # !! - many liveries are not weathered as they don't use the remap callback
        # !! - so for strict behaviour this should only be applied to liveries that have colour_set_names??
        # !! - as of April 2025, this was working, so JFDI for now
        force_no_weathering = False
        if livery_name.endswith("_NO_WEATHERING"):
            livery_name = livery_name.removesuffix("_NO_WEATHERING")
            force_no_weathering = True

        try:
            livery_def = self[livery_name]
        except KeyError as e:
            raise ValueError(
                f"Livery '{livery_name}' not found in LiverySupplier"
            ) from e

        use_weathering = False if force_no_weathering else livery_def.use_weathering
        livery = replace(
            livery_def,
            relative_spriterow_num=relative_spriterow_num,
            use_weathering=use_weathering,
        )

        self.delivered_liveries.append(livery_name)
        return livery

    @cached_property
    def freight_wagon_liveries(self):
        return {
            livery_name: livery
            for livery_name, livery in self.items()
            if livery.is_freight_wagon_livery
        }

    def freight_wagon_livery_index(self, livery_name, context=None):
        # look up the index of a livery in the subset of freight wagon liveries
        livery_index = list(self.freight_wagon_liveries).index(livery_name)
        if context == "purchase":
            # purchase livery indexes are appended after the list of non-purchase liveries, so offset appropriately
            livery_index = len(self.freight_wagon_liveries) + livery_index
        return livery_index

    @cached_property
    def freight_livery_colour_set_indexes_and_names(self):
        result = {
            "company_colour": 100,
            "complement_company_colour": 101,
        }
        for index, colour_set_name in enumerate(list(global_constants.colour_sets)):
            result[colour_set_name] = index
        return result

    def serialize_livery_params(self, flag_context_is_purchase, colour_set_indexes):
        # flatten to numeric params for nml templating
        livery_result = [
            flag_context_is_purchase,
        ]
        # length of colour_set_indexes *must* be 8, as we have up to 8 liveries per buyable wagon variant, and we must provide values for 8 registers
        colour_set_indexes = list(islice(cycle(colour_set_indexes), 8))
        livery_result.extend(colour_set_indexes)
        # we flatten to string for ease of rendering in nml template
        # int used to convert False|True bools to 0|1 values for nml
        serialized_params = ", ".join(str(int(i)) for i in livery_result)
        return serialized_params

    @property
    def freight_wagon_livery_serialized_params(self):
        # we need to serialize liveries to numeric params for nml, we do this once and create a lookup table
        result = []
        # first append all the actual liveries, serialized for nml params, with index for access
        for livery_name, livery in self.freight_wagon_liveries.items():
            colour_set_indexes = []
            for colour_set_name in livery.colour_set_names:
                colour_set_indexes.append(
                    self.freight_livery_colour_set_indexes_and_names[colour_set_name]
                )
            serialized_params = self.serialize_livery_params(
                flag_context_is_purchase=False,
                colour_set_indexes=colour_set_indexes,
            )
            livery_index = self.freight_wagon_livery_index(livery_name)
            result.append(
                {
                    "livery_name": livery_name,  # for convenient debugging
                    "livery_index": livery_index,
                    "serialized_params": serialized_params,
                }
            )
        # then append purchase variants of each livery, in same order
        for livery_name, livery in self.freight_wagon_liveries.items():
            if len(livery.purchase_swatch_colour_set_names) > 0:
                colour_set_name = livery.purchase_swatch_colour_set_names[0]
            else:
                # otherwise take the first colour set as default for purchase
                colour_set_name = livery.colour_set_names[0]
            purchase_livery_index = self.freight_livery_colour_set_indexes_and_names[
                colour_set_name
            ]
            # we still use the list of colour set indexes, but one entry is enough for purchase, the entries will be auto-repeated by the serializer
            colour_set_indexes = [purchase_livery_index]
            serialized_params = self.serialize_livery_params(
                flag_context_is_purchase=True,
                colour_set_indexes=colour_set_indexes,
            )
            # purchase livery indexes are appended after the list of non-purchase liveries, so offset appropriately
            livery_index = len(
                self.freight_wagon_liveries
            ) + self.freight_wagon_livery_index(livery_name)
            result.append(
                {
                    "livery_name": f"Purchase - {livery_name}",  # for convenient debugging
                    "livery_index": livery_index,
                    "serialized_params": serialized_params,
                }
            )
        return result

    @property
    def consolidated_liveries_for_badge_display(self):
        # some liveries are near-identical, differing only in random vs. non-random, or very minor differences in colour sets
        # therefore we consolidate those to reduce badge noise when filtering vehicles
        result = []
        seen_purchase_swatches = []
        for livery in self.values():
            if not livery.is_freight_wagon_livery:
                if livery.proxy_livery_for_badge_display_and_filter is not None:
                    #result.append(livery)
                    result.append(self[livery.proxy_livery_for_badge_display_and_filter])
                else:
                    result.append(livery)
            else:
                if livery.purchase_swatch not in seen_purchase_swatches:
                    result.append(livery)
                    seen_purchase_swatches.append(livery.purchase_swatch)
                else:
                    if livery.proxy_livery_for_badge_display_and_filter is not None:
                        #result.append(livery)
                        result.append(self[livery.proxy_livery_for_badge_display_and_filter])
                    else:
                        # this is JFDI, and might choke on livery order, or multiple liveries declaring same proxy_livery_for_badge_display_and_filter
                        raise Exception(
                            f"Livery {livery.livery_name} will duplicate badges with another livery that uses {livery.purchase_swatch}"
                            "\n to resolve this add proxy_livery_for_badge_display_and_filter value to the livery def"
                        )
        return result

    def report_unused_liveries(self):
        for livery in self.keys():
            if livery not in self.delivered_liveries:
                print("Unused", livery)
