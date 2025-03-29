from dataclasses import dataclass, field, replace
from typing import Any, Dict, List, Optional


@dataclass
class LiveryDef:
    # CABBAGE SPARSE CLASS
    livery_name: str
    # alphabetised optional attrs
    colour_set: Optional[str] = None
    docs_image_input_cc: Optional[List] = None
    purchase: Optional[str] = None
    relative_spriterow_num: Optional[int] = None
    remap_to_cc: Optional[str] = None
    use_weathering: Optional[bool] = False


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
