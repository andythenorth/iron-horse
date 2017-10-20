import global_constants
from train import CabooseConsist, CabooseCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    consist = CabooseConsist(roster='pony',
                             base_numeric_id=1290,
                             gen=1,
                             subtype='A',
                             track_type='NG')

    consist.add_unit(type=CabooseCar,
                     vehicle_length=4)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    #--------------- pony ----------------------------------------------------------------------
    consist = CabooseConsist(roster='pony',
                             base_numeric_id=1280,
                             gen=1,
                             subtype='A')

    consist.add_unit(type=CabooseCar,
                     vehicle_length=4)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = CabooseConsist(roster='pony',
                             base_numeric_id=2210,
                             gen=1,
                             subtype='B')

    consist.add_unit(type=CabooseCar,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)


"""
    #--------------- llama ----------------------------------------------------------------------
    consist = CabooseConsist(title = '[Caboose Car]',
                             roster = 'llama',
                             base_numeric_id = 1300,
                             gen = 1)

    consist.add_unit(type = CabooseCar,
                            vehicle_length = 5)

    consist.add_model_variant(start_date = 0,
                              end_date = global_constants.max_game_date)


    #--------------- antelope ----------------------------------------------------------------------
    consist = CabooseConsist(title = '[Caboose Car]',
                             roster = 'antelope',
                             base_numeric_id = 1780,
                             gen = 1)

    consist.add_unit(type = CabooseCar,
                           vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                              end_date = global_constants.max_game_date)


    consist = CabooseConsist(title = '[Caboose Car]',
                             roster = 'antelope',
                             base_numeric_id = 1880,
                             gen = 1,
                             track_type = 'NG')

    consist.add_unit(type = CabooseCar,
                           vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                              end_date = global_constants.max_game_date)


"""
