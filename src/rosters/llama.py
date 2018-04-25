from roster import Roster

from vehicles import ge289a
from vehicles import americano
from vehicles import anaconda
from vehicles import argentina
from vehicles import astarsa
from vehicles import baldwin
from vehicles import breda
from vehicles import burro
from vehicles import cooke
from vehicles import cooper
from vehicles import electrico
from vehicles import estados
from vehicles import evolucao
from vehicles import justicialista
from vehicles import krauss
from vehicles import manzana
from vehicles import medrano
from vehicles import pacifico
from vehicles import pala
from vehicles import patagonia
from vehicles import peacock
from vehicles import pequeno
from vehicles import potosi
from vehicles import riachuelo
from vehicles import roca
from vehicles import super_mountain
from vehicles import universal
from vehicles import ut440
from vehicles import v8

# !! needs refactored to match Pony
# speed for wagons in mph (some generations may optionally have no speed set)
# format is [standard, speedy]
speeds = dict(gen_1_wagon_speeds = [50, 65],
              gen_2_wagon_speeds = [60, 85],
              gen_3_wagon_speeds = [70, 100],
              ng_gen_1_wagon_speeds = [35, 45],
              ng_gen_2_wagon_speeds = [45, 55],
              ng_gen_3_wagon_speeds = [55, 65])

roster = Roster(id = 'llama',
                numeric_id = 2,
                speeds = speeds, # hax
                # capacity factor per generation, will be multiplied by vehicle length
                freight_car_capacity_per_unit_length =  {'RAIL': [5, 5, 5, 5, 5, 5],
                                                         'NG': [3, 3, 3, 3, 3, 3]},
                engines = [burro,
                           americano,
                           peacock,
                           cooke,
                           pacifico,
                           argentina,
                           potosi,
                           super_mountain,
                           electrico,
                           estados,
                           breda,
                           v8,
                           ut440,
                           justicialista,
                           pequeno,
                           baldwin,
                           ge289a,
                           cooper,
                           krauss,
                           pala,
                           astarsa,
                           universal,
                           evolucao,
                           roca,
                           anaconda,
                           patagonia,
                           riachuelo,
                           manzana,
                           medrano])
