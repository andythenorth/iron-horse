from roster import Roster

from vehicles import aberdare
from vehicles import bertha
from vehicles import cargo_sprinter
from vehicles import chaplin
from vehicles import chinook
from vehicles import cyclops
from vehicles import donegal
from vehicles import double_juice
from vehicles import electra
from vehicles import fleet
from vehicles import gridiron
from vehicles import high_flyer
from vehicles import hudswell
from vehicles import lemon
from vehicles import little_bear
from vehicles import mole
from vehicles import northcock
from vehicles import ramsbottom
from vehicles import raven
from vehicles import screamer
from vehicles import serpentine
from vehicles import slammer
from vehicles import standard
from vehicles import stewart
from vehicles import suburban
from vehicles import tin_rocket
from vehicles import vulcan
from vehicles import walker
from vehicles import westbourne

# speed for wagons in mph (some generations may optionally have no speed set)
# format is [standard, speedy]
speeds = dict(gen_1_wagon_speeds = [65, 85],
              gen_2_wagon_speeds = [85, 100],
              gen_3_wagon_speeds = [100, None],
              ng_gen_1_wagon_speeds = [55, 55])

roster = Roster(id = 'brit',
                numeric_id = 1,
                speeds = speeds,
                engines = [chaplin,
                           standard,
                           ramsbottom,
                           bertha,
                           high_flyer,
                           aberdare,
                           raven,
                           suburban,
                           northcock,
                           lemon,
                           electra,
                           chinook,
                           vulcan,
                           little_bear,
                           gridiron,
                           screamer,
                           cargo_sprinter,
                           double_juice,
                           cyclops,
                           slammer,
                           tin_rocket,
                           # brit extras
                           serpentine,
                           westbourne,
                           fleet,
                           mole,
                           # brit ng
                           stewart,
                           hudswell,
                           donegal,
                           walker])
