from roster import Roster

from vehicles import americano
from vehicles import argentina
from vehicles import astarsa
from vehicles import breda
from vehicles import burro
from vehicles import cooke
from vehicles import electrico
from vehicles import estados
from vehicles import evolucao
from vehicles import justicialista
from vehicles import krauss
from vehicles import pacifico
from vehicles import pala
from vehicles import peacock
from vehicles import roca
from vehicles import super_mountain
from vehicles import thing_ng
from vehicles import universal
from vehicles import ut440
from vehicles import v8

roster = Roster(id = 'soam',
                buy_menu_sort_order = [thing_ng.consist.id,
                                       burro.consist.id,
                                       americano.consist.id,
                                       peacock.consist.id,
                                       cooke.consist.id,
                                       pacifico.consist.id,
                                       argentina.consist.id,
                                       super_mountain.consist.id,
                                       electrico.consist.id,
                                       estados.consist.id,
                                       breda.consist.id,
                                       v8.consist.id,
                                       ut440.consist.id,
                                       justicialista.consist.id,
                                       krauss.consist.id,
                                       pala.consist.id,
                                       astarsa.consist.id,
                                       universal.consist.id,
                                       evolucao.consist.id,
                                       roca.consist.id])
