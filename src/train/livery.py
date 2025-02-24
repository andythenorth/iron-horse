from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

@dataclass
class LiveryDef:
    # CABBAGE SPARSE CLASS
    # alphabetised attrs
    colour_set: Optional[str] = None
    docs_image_input_cc: Optional[List] = None
    purchase: Optional[str] = None
    relative_spriterow_num: Optional[int] = None
    remap_to_cc: Optional[str] = None
    use_weathering: Optional[bool] = False


