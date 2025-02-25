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
        # if not a duplicate, add the livery
        if livery_name in self:
            # CABBAGE - FIGURE OUT LATER WHETHER TO ALLOW REDEFINING BY ROSTERS, OR WHETHER TO FORCE A COMMON LIVERY SET
            if livery_name in ["VANILLA", "SWOOSH", "FOO", "TGV_LA_POSTE"]:
                print(
                    f"LiverySupplier.add_livery: a roster tried to add {livery_name} when it already exists"
                )
            else:
                raise ValueError(
                    f"LiverySupplier.add_livery: a roster tried to add {livery_name} when it already exists"
                )
        else:
            # note we store livery_name in LiveryDef, but we also use it as the dict key for easy access, this is duplication, but fine, livery names are immutable by convention
            self[livery_name] = LiveryDef(livery_name, **kwargs)
        # no return as of now, not needed

    def deliver(self, livery_name: str, relative_spriterow_num: int):
        # Return a modified copy of the canonical LiveryDef identified by livery_name.

        try:
            livery_def = self[livery_name]
        except KeyError:
            raise ValueError(f"Livery '{livery_name}' not found in LiverySupplier")
        return replace(livery_def, relative_spriterow_num=relative_spriterow_num)
