from train import StakeCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = StakeCarConsist(roster='pony',
                           base_numeric_id=2740,
                           gen=2,
                           subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = StakeCarConsist(roster='pony',
                           base_numeric_id=2730,
                           gen=3,
                           subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = StakeCarConsist(roster='pony',
                           base_numeric_id=2750,
                           gen=3,
                           subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = StakeCarConsist(roster='pony',
                           base_numeric_id=1710,
                           gen=4,
                           subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = StakeCarConsist(roster='pony',
                           base_numeric_id=2760,
                           gen=4,
                           subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = StakeCarConsist(roster='pony',
                           base_numeric_id=930,
                           gen=5,
                           subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = StakeCarConsist(roster='pony',
                           base_numeric_id=2770,
                           gen=5,
                           subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    # no gen 6 stake cars, cap to gen 5 in Pony

    # --------------- antelope ----------------------------------------------------------------------

    #--------------- llama ----------------------------------------------------------------------
