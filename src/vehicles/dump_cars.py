from train import DumpCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = DumpCarConsist(roster='pony',
                             base_numeric_id=2350,
                             gen=3,
                             subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = DumpCarConsist(roster='pony',
                             base_numeric_id=2360,
                             gen=3,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = DumpCarConsist(roster='pony',
                             base_numeric_id=2370,
                             gen=4,
                             subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = DumpCarConsist(roster='pony',
                             base_numeric_id=2380,
                             gen=4,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = DumpCarConsist(roster='pony',
                             base_numeric_id=1340,
                             gen=5,
                             subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = DumpCarConsist(roster='pony',
                             base_numeric_id=1810,
                             gen=5,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = DumpCarConsist(roster='pony',
                             base_numeric_id=2400,
                             gen=6,
                             subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = DumpCarConsist(roster='pony',
                             base_numeric_id=2390,
                             gen=6,
                             subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)

    #--------------- llama ----------------------------------------------------------------------

    #--------------- antelope ----------------------------------------------------------------------
