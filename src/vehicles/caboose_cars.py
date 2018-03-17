from train import CabooseCarConsist, CabooseCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    consist = CabooseCarConsist(roster='pony',
                                base_numeric_id=1290,
                                gen=1,
                                subtype='A',
                                track_type='NG')

    consist.add_unit(type=CabooseCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0)

    #--------------- pony ----------------------------------------------------------------------
    consist = CabooseCarConsist(roster='pony',
                                base_numeric_id=1280,
                                gen=1,
                                subtype='A')

    consist.add_unit(type=CabooseCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = CabooseCarConsist(roster='pony',
                                base_numeric_id=2210,
                                gen=1,
                                subtype='B')

    consist.add_unit(type=CabooseCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)


"""
    #--------------- llama ----------------------------------------------------------------------
    consist = CabooseCarConsist(title = '[Caboose Car]',
                             roster = 'llama',
                             base_numeric_id = 1300,
                             gen = 1)

    consist.add_unit(type = CabooseCar,
                            vehicle_length = 5)

    consist.add_model_variant(spritesheet_suffix=0)


    #--------------- antelope ----------------------------------------------------------------------
    consist = CabooseCarConsist(title = '[Caboose Car]',
                             roster = 'antelope',
                             base_numeric_id = 1780,
                             gen = 1)

    consist.add_unit(type = CabooseCar,
                           vehicle_length = 6)

    consist.add_model_variant(spritesheet_suffix=0)


    consist = CabooseCarConsist(title = '[Caboose Car]',
                             roster = 'antelope',
                             base_numeric_id = 1880,
                             gen = 1,
                             track_type = 'NG')

    consist.add_unit(type = CabooseCar,
                           vehicle_length = 6)

    consist.add_model_variant(spritesheet_suffix=0)


"""
