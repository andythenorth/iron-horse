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
from vehicles import growler
from vehicles import high_flyer
from vehicles import hudswell
from vehicles import lemon
from vehicles import little_bear
from vehicles import longwater
from vehicles import northcock
from vehicles import ramsbottom
from vehicles import raven
from vehicles import roarer
from vehicles import screamer
from vehicles import serpentine
from vehicles import slammer
from vehicles import standard
from vehicles import stewart
from vehicles import suburban
from vehicles import tideway
from vehicles import tin_rocket
from vehicles import tyburn
from vehicles import walker
from vehicles import westbourne
from vehicles import wizzo

# speed for wagons in mph (some generations may optionally have no speed set)
# format is [standard, speedy]
# speeds are roughly matched to RH trucks of same era + 5mph or so
speeds = dict(gen_1_wagon_speeds = [45, 90],
              gen_2_wagon_speeds = [60, 90],
              gen_3_wagon_speeds = [75, None],
              ng_gen_1_wagon_speeds = [55, 55])

roster = Roster(id = 'pony',
                numeric_id = 1,
                speeds = speeds,
                engines = [chaplin,
                           ramsbottom,
                           bertha,
                           standard,
                           suburban,
                           aberdare,
                           high_flyer,
                           raven,
                           lemon,
                           northcock,
                           electra,
                           little_bear,
                           growler,
                           chinook,
                           wizzo,
                           roarer,
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
                           longwater,
                           tyburn,
                           tideway,
                           # brit ng
                           stewart,
                           hudswell,
                           donegal,
                           walker])
