from roster import Roster

#from vehicles import aberdare

# speed for wagons in mph (some generations may optionally have no speed set)
# format is [standard, speedy]
speeds = dict(gen_1_wagon_speeds = [65, 85],
              gen_2_wagon_speeds = [85, 100],
              gen_3_wagon_speeds = [100, None],
              ng_gen_1_wagon_speeds = [55, 55])

roster = Roster(id = 'antelope',
                numeric_id = 2,
                speeds = speeds,
                engines = [])
