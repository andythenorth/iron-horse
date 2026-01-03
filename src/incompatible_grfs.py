from utils import DwordGrfID as DwordGrfID
from utils import LiteralGrfID as LiteralGrfID

incompatible_grfs = []


class IncompatibleGRF(object):
    """simple class to hold incompatible grfs, including optional properties for extended checks"""

    def __init__(self, grfid, grfname):
        self._grfid = (
            grfid  # private var for this, we'll mangle it when called as a property
        )
        self.grfname = grfname
        incompatible_grfs.append(self)

    @property
    def grfid(self):
        return self._grfid.grfid


# add incompatible grfs here (note that some properties are optional, allowing simple or extended checks)
# IMPORTANT
# both forms of grfid string are supported: literal (per nfo) and dword (displayed in Bananas, in OpenTTD)

# !! CABBAGE - railtypes aren't incompatible - this is disabling on a load order check - refactor names?
IncompatibleGRF(DwordGrfID("595AAA02"), "JP+ Tracks")
IncompatibleGRF(DwordGrfID("42424e54"), "SETS: Narrow gauge")
IncompatibleGRF(DwordGrfID("42425354"), "SETS: Standard gauge")
