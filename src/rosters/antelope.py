from roster import Roster

from vehicles import antlion
from vehicles import savannah_slammer

# speed for wagons in mph (some generations may optionally have no speed set)
# format is [standard, speedy]
speeds = dict(gen_1_wagon_speeds = [55, 75],
              gen_2_wagon_speeds = [75, 75],
              ng_gen_1_wagon_speeds = [55, 55])

roster = Roster(id = 'antelope',
                numeric_id = 3,
                speeds = speeds,
                engines = [antlion,
                           savannah_slammer])
