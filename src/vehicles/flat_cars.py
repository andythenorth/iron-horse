from train import FlatCarConsist, FreightCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=1170,
                             gen=1,
                             subtype='A',
                             track_type='NG')

    consist.add_unit(type=FreightCar,
                     cargo_length=3,
                     vehicle_length=3)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    #--------------- pony ----------------------------------------------------------------------
    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=1140,
                             gen=1,
                             subtype='A')

    consist.add_unit(type=FreightCar,
                     cargo_length=3,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=1150,
                             gen=2,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     cargo_length=3,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=1160,
                             gen=3,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     cargo_length=3,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=2550,
                             gen=3,
                             subtype='C')

    consist.add_unit(type=FreightCar,
                     cargo_length=3,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=2540,
                             gen=4,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     cargo_length=3,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=2530,
                             gen=4,
                             subtype='C')

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=2520,
                             gen=5,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     cargo_length=3,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = FlatCarConsist(roster='pony',
                             base_numeric_id=2510,
                             gen=5,
                             subtype='C')

    consist.add_unit(type=FreightCar,
                     cargo_length=4,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    # no gen 6 flat cars, cap to gen 5 in Pony

    #--------------- llama ----------------------------------------------------------------------
    consist = FlatCarConsist(roster='llama',
                             base_numeric_id=1180,
                             gen=1,
                             subtype='A')

    consist.add_unit(type=FreightCar,
                     cargo_length=3,
                     vehicle_length=5)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = FlatCarConsist(roster='llama',
                             base_numeric_id=1510,
                             gen=2,
                             subtype='A')

    consist.add_unit(type=FreightCar,
                     cargo_length=3,
                     vehicle_length=5)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = FlatCarConsist(roster='llama',
                             base_numeric_id=520,
                             gen=1,
                             subtype='A',
                             track_type='NG')

    consist.add_unit(type=FreightCar,
                     cargo_length=3,
                     vehicle_length=5)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = FlatCarConsist(roster='llama',
                             base_numeric_id=1500,
                             gen=2,
                             subtype='A',
                             track_type='NG')

    consist.add_unit(type=FreightCar,
                     cargo_length=3,
                     vehicle_length=5)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    #--------------- antelope ----------------------------------------------------------------------
    consist = FlatCarConsist(roster='antelope',
                             base_numeric_id=1640,
                             gen=1,
                             subtype='A')

    consist.add_unit(type=FreightCar,
                     cargo_length=3,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = FlatCarConsist(roster='antelope',
                             base_numeric_id=1650,
                             gen=2,
                             subtype='A')

    consist.add_unit(type=FreightCar,
                     cargo_length=3,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = FlatCarConsist(roster='antelope',
                             base_numeric_id=2110,
                             gen=1,
                             subtype='A',
                             track_type='NG')

    consist.add_unit(type=FreightCar,
                     cargo_length=3,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = FlatCarConsist(roster='antelope',
                             base_numeric_id=1930,
                             gen=2,
                             subtype='A',
                             track_type='NG')

    consist.add_unit(type=FreightCar,
                     cargo_length=3,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])
