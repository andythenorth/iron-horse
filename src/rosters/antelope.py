from roster import Roster

from vehicles import albertine
from vehicles import antlion
from vehicles import baby_boat
from vehicles import big_boat
from vehicles import bigfoot
from vehicles import bush_elephant
from vehicles import drakensberg
from vehicles import gazelle
from vehicles import hippo
from vehicles import hofman
from vehicles import kessler
from vehicles import kwa_falls
from vehicles import milne
from vehicles import ndemi
from vehicles import okapi
from vehicles import oribi
from vehicles import oubangui
from vehicles import pangolin
from vehicles import savannah_slammer
from vehicles import smokey_mountain
from vehicles import springburn
from vehicles import waterbuck

# speed for wagons in mph (some generations may optionally have no speed set)
# format is [standard, speedy]
speeds = dict(gen_1_wagon_speeds = [55, None], # no point setting an upper speed for SG in this roster, max engine is always 75mph
              gen_2_wagon_speeds = [75, None],
              ng_gen_1_wagon_speeds = [35, 55], # this roster is deliberately slow for NG freight
              ng_gen_2_wagon_speeds = [45, 75],
              ng_gen_3_wagon_speeds = [55, 95])

roster = Roster(id = 'antelope',
                numeric_id = 3,
                speeds = speeds,
                engines = [kessler,
                           pangolin,
                           albertine,
                           ndemi,
                           milne,
                           bush_elephant,
                           oubangui,
                           hofman,
                           kwa_falls,
                           drakensberg,
                           okapi,
                           bigfoot,
                           gazelle,
                           hippo,
                           waterbuck,
                           oribi,
                           springburn,
                           smokey_mountain,
                           baby_boat,
                           big_boat,
                           antlion,
                           savannah_slammer])
