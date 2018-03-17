from train import SiloCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = SiloCarConsist(roster='pony',
                             base_numeric_id=2950,
                             gen=4,
                             subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = SiloCarConsist(roster='pony',
                             base_numeric_id=2980,
                             gen=5,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = SiloCarConsist(roster='pony',
                             base_numeric_id=2960,
                             gen=5,
                             subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)
    #--------------- llama ----------------------------------------------------------------------

    #--------------- antelope ----------------------------------------------------------------------
