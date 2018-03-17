from train import IntermodalCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = IntermodalCarConsist(roster='pony',
                                   base_numeric_id=1060,
                                   gen=4,
                                   subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = IntermodalCarConsist(roster='pony',
                                   base_numeric_id=2800,
                                   gen=4,
                                   subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = IntermodalCarConsist(roster='pony',
                                   base_numeric_id=2810,
                                   gen=5,
                                   subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = IntermodalCarConsist(roster='pony',
                                   base_numeric_id=2820,
                                   gen=5,
                                   subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = IntermodalCarConsist(roster='pony',
                                   base_numeric_id=2830,
                                   gen=6,
                                   subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = IntermodalCarConsist(roster='pony',
                                   base_numeric_id=2840,
                                   gen=6,
                                   subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)

    #--------------- llama ----------------------------------------------------------------------
