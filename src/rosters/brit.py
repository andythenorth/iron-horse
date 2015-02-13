from roster import Roster

from vehicles import cargo_sprinter
from vehicles import chaplin
from vehicles import chinook
from vehicles import collier
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

roster = Roster(id = 'brit',
                buy_menu_sort_order = [chaplin.consist.id,
                                       standard.consist.id,
                                       ramsbottom.consist.id,
                                       collier.consist.id,
                                       high_flyer.consist.id,
                                       raven.consist.id,
                                       suburban.consist.id,
                                       northcock.consist.id,
                                       lemon.consist.id,
                                       electra.consist.id,
                                       chinook.consist.id,
                                       vulcan.consist.id,
                                       little_bear.consist.id,
                                       gridiron.consist.id,
                                       screamer.consist.id,
                                       cargo_sprinter.consist.id,
                                       double_juice.consist.id,
                                       cyclops.consist.id,
                                       slammer.consist.id,
                                       tin_rocket.consist.id,
                                       # brit extras
                                       serpentine.consist.id,
                                       westbourne.consist.id,
                                       fleet.consist.id,
                                       mole.consist.id,
                                       'metro_car_brit_gen_1', # special case, non-standard naming, and this is explicitly placed after metro locos, unlike most cars which are automatically placed in buy menu
                                       # brit ng
                                       stewart.consist.id,
                                       hudswell.consist.id,
                                       donegal.consist.id,
                                       walker.consist.id])
