from train import FruitVegCarConsist, FreightCar


def main():
    #--------------- pony --------------------------------------------------------------------------
    consist = FruitVegCarConsist(roster='pony',
                                 base_numeric_id=2640,
                                 gen=2,
                                 subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = FruitVegCarConsist(roster='pony',
                                 base_numeric_id=2630,
                                 gen=3,
                                 subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = FruitVegCarConsist(roster='pony',
                                 base_numeric_id=2620,
                                 gen=3,
                                 subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = FruitVegCarConsist(roster='pony',
                                 base_numeric_id=2600,
                                 gen=4,
                                 subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = FruitVegCarConsist(roster='pony',
                                 base_numeric_id=2610,
                                 gen=4,
                                 subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = FruitVegCarConsist(roster='pony',
                                 base_numeric_id=2650,
                                 gen=5,
                                 subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = FruitVegCarConsist(roster='pony',
                                 base_numeric_id=2660,
                                 gen=5,
                                 subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)

    # no gen 6 fruit & veg cars, cap to gen 5 in Pony

    #--------------- antelope ----------------------------------------------------------------------
    consist = FruitVegCarConsist(roster='antelope',
                                 base_numeric_id=2140,
                                 gen=1,
                                 subtype='A',
                                 track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=5)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = FruitVegCarConsist(roster='antelope',
                                 base_numeric_id=2170,
                                 gen=2,
                                 subtype='A',
                                 track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = FruitVegCarConsist(roster='antelope',
                                 base_numeric_id=2180,
                                 gen=3,
                                 subtype='A',
                                 track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)
