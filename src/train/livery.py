from dataclasses import dataclass, field, replace
from typing import Any, Dict, List, Optional
from itertools import cycle, islice

import global_constants


@dataclass
class LiveryDef:
    # CABBAGE SPARSE CLASS
    livery_name: str
    # alphabetised optional attrs
    colour_set_names: Optional[str] = None
    purchase_colour_set_names: Optional[str] = None
    docs_image_input_cc: Optional[List] = None
    relative_spriterow_num: Optional[int] = None
    remap_to_cc: Optional[str] = None
    use_weathering: Optional[bool] = False
    is_freight_wagon_livery: Optional[bool] = False


class LiverySupplier(dict):
    """
    A lightweight supplier of canonical LiveryDef instances.

    This class stores LiveryDef instances keyed by their immutable livery names.
    It allows efficient lookup and delivers modified copies of these instances on demand.
    Intended for use as a singleton in contexts such as templates or compile-time operations.
    """

    def add_livery(self, livery_name: str, **kwargs):
        livery = LiveryDef(livery_name, **kwargs)
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

        try:
            livery_def = self[livery_name]
        except KeyError:
            raise ValueError(f"Livery '{livery_name}' not found in LiverySupplier")
        return replace(livery_def, relative_spriterow_num=relative_spriterow_num)

    @property
    def freight_wagon_liveries(self):
        return {
            livery_name: livery
            for livery_name, livery in self.items()
            if livery.is_freight_wagon_livery
        }

    def freight_wagon_livery_index(self, livery_name, context=None):
        # look up the index of a livery in the subset of freight wagon liveries
        return list(self.freight_wagon_liveries).index(livery_name)

    @property
    def cabbage_valid_freight_livery_colour_set_names_and_nums(self):
        result = {
            "company_colour": 100,
            "complement_company_colour": 101,
        }
        for index, colour_set_name in enumerate(list(global_constants.colour_sets)):
            result[colour_set_name] = index
        return result

    @property
    def freight_wagon_livery_serialized_params(self):
        result = []
        for livery_name, livery in self.freight_wagon_liveries.items():
            if not isinstance(livery.colour_set_names, list):
                raise ValueError(livery)
            flag_use_weathering = livery.use_weathering
            # CABBAGE
            # flag_context_is_purchase = True if context == "purchase" else False
            # MAYBE add 100 to livery num if context purchase?
            flag_context_is_purchase = False  # SHIM
            wagon_recolour_strategy_num_purchase = 104  # CABBAGE SHIM

            livery_result = [
                flag_use_weathering,
                flag_context_is_purchase,
                wagon_recolour_strategy_num_purchase,
            ]
            colour_set_indexes = []
            for colour_set_name in livery.colour_set_names:
                colour_set_indexes.append(
                    self.cabbage_valid_freight_livery_colour_set_names_and_nums[
                        colour_set_name
                    ]
                )
            # length of colour_set_indexes *must* be 8, as we have up to 8 liveries per buyable wagon variant, and we must provide values for 8 registers
            colour_set_indexes = list(islice(cycle(colour_set_indexes), 8))
            livery_result.extend(colour_set_indexes)
            # int used to convert False|True bools to 0|1 values for nml
            serialized_params = ", ".join(str(int(i)) for i in livery_result)
            # we could do this without the index, and set it in the templating loop, but this is just cleaner
            result.append(
                {
                    "livery_name": livery_name,  # for convenient debugging
                    "livery_index": self.freight_wagon_livery_index(livery_name),
                    "serialized_params": serialized_params,
                }
            )
        return result

    """
    def get_wagon_recolour_strategy_params(self, context=None):
        # CABBAGE - THIS RETURNS PARAMS WHICH ARE THEN COMPRESSED TO AN INDEX AND EXPANDED LATER (FOR NML PERFORMANCE REASONS)

        if self.uses_random_livery:
            # CABBAGE get_candidate_liveries_for_randomised_strategy is deleted - just get liveries from colour_set_names, stop arsing around
            available_liveries = self.get_candidate_liveries_for_randomised_strategy(
                self.catalogue_entry.livery_def
            )
            if self.catalogue_entry.livery_def.purchase is not None:
                wagon_recolour_strategy_num_purchase = (
                    self.get_wagon_recolour_strategy_num(
                        self.catalogue_entry.livery_def, context="purchase"
                    )
                )
            else:
                wagon_recolour_strategy_num_purchase = available_liveries[0]
        else:
            # we have to provide 8 options for nml params, but in this case they are all unused, so just pass them as 0
            available_liveries = [0, 0, 0, 0, 0, 0, 0, 0]
            # purchase strategy will be same as non-purchase
            CABBAGE = CABBAGE

        flag_use_weathering = self.catalogue_entry.livery_def.use_weathering
        flag_context_is_purchase = True if context == "purchase" else False

        params_numeric = [
            flag_use_weathering,
            flag_context_is_purchase,
            wagon_recolour_strategy_num_purchase,
        ]

        params_numeric.extend(available_liveries)

        # int used to convert False|True bools to 0|1 values for nml
        return ", ".join(str(int(i)) for i in params_numeric)
    """

    """
    def compute_wagon_recolour_sets(self):
        # wagon recolour liveries can be randomised across multiple colour sets
        # this is a run-time randomisation, relying on a procedure that takes parameters for the candidate livery numbers
        # however there are 10 parameters, and calls to the procedure are needed thousands of times per grf,
        # testing proved that generating thousands of procedure calls with 10 params directly in the nml was expensive in file size, both nml and grf
        # there are however a finite number of combinations that are actually needed (only 125 as of Sept 2024)
        # therefore we can provide a compile-time lookup table, and index into it using a procedure call with a single parameter
        # this does not have the same cost in nml or grf filesize
        # CABBAGE CAN THIS BE DERIVED FROM LIVERIES NOW?
        # WHAT ARE THE PARAMS?  - COLOURS, WEATHERING?
        print("len(freight_wagon_liveries)", len(global_constants.freight_wagon_liveries))
        # CABBAGE JUST MAP DIRECTLY TO THE LIVERIES from global_constants.freight_wagon_liveries
        # THE LU TABLE HAS THE PARAMS?
        # AND WE JUST NEED THE LIVERY NUMBER?
        # freight_wagon_liveries is a dict, but just rely on key position, probably fine?
        # MOVE THIS to LiverySupplier?
        seen_params = []
        for wagon_model_variant in self.wagon_model_variants:
            if getattr(
                wagon_model_variant, "use_colour_randomisation_strategies", False
            ):
                seen_params.append(
                    wagon_model_variant.get_wagon_recolour_strategy_params()
                )
                seen_params.append(
                    wagon_model_variant.get_wagon_recolour_strategy_params(
                        context="purchase"
                    )
                )

        self.freight_wagon_livery_serialized_params = list(set(seen_params))
    """

    """

    def get_candidate_liveries_for_randomised_strategy(self, livery):
        # CABBAGE - THIS WALKS A RANDOMISED LIVERY, AND SELECTS ONLY THOSE REMAPS WHICH THE VEHICLE ACTUALLY USES IN NON-RANDOMISED LIVERIES
        # DO WE CARE ABOUT PRESERVING THAT BEHAVIOUR?  OR IS RANDOM LITERALLY JUST RANDOM FROM A LIST?
        # HMM
        # RANDOM_LIVERIES_VARIETY *DOES* DEPEND ON THE OTHER LIVERIES FOR THE CANDIDATES - CHANGE? DELETE?
        # this will only work with wagon liveries as of April 2023, and is intended to get remaps only
        result = []
        for cabbage_candidate_livery in self.catalogue_entry.catalogue:
            if (
                cabbage_candidate_livery.livery_def.colour_set_names
                in global_constants.wagon_livery_mixes[livery.colour_set_names]
            ):
                candidate_livery_strategy_num = self.get_wagon_recolour_strategy_num(
                    cabbage_candidate_livery.livery_def
                )
                result.append(candidate_livery_strategy_num)
        # length of result *must* be 8, as we have up to 8 liveries per buyable wagon variant, and we must provide values for 8 registers
        # this just crudely extends the list, repeating values as needed
        extension = result[0 : 8 - len(result)]
        if len(extension) == 0:
            raise BaseException(
                self.id
                + " get_candidate_liveries_for_randomised_strategy: extension list too short "
                + str(extension)
                + "; \n this is probably because we're slicing 8, and have more than 8 colours defined; which will fail;"
                + "; \n there are now more random bits available for OpenTTD 14 so this might be solvable"
            )
        # !! it's possible this doesn't close
        while len(result) < 8:
            result.extend(extension)
        # yes, I'm sure we could avoid over-extending and then slicing the list, but eh, life is short
        if (len(result)) > 8:
            result = result[0:8]
        return result

    """
