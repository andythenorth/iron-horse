from train import SuppliesCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = SuppliesCarConsist(roster='pony',
                                 base_numeric_id=710,
                                 gen=2,
                                 subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = SuppliesCarConsist(roster='pony',
                                 base_numeric_id=700,
                                 gen=3,
                                 subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = SuppliesCarConsist(roster='pony',
                                 base_numeric_id=2850,
                                 gen=3,
                                 subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = SuppliesCarConsist(roster='pony',
                                 base_numeric_id=2860,
                                 gen=4,
                                 subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = SuppliesCarConsist(roster='pony',
                                 base_numeric_id=2870,
                                 gen=4,
                                 subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = SuppliesCarConsist(roster='pony',
                                 base_numeric_id=2880,
                                 gen=5,
                                 subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = SuppliesCarConsist(roster='pony',
                                 base_numeric_id=2890,
                                 gen=5,
                                 subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = SuppliesCarConsist(roster='pony',
                                 base_numeric_id=2690,
                                 gen=5,
                                 subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)

    # no gen 6 supplies cars, cap to gen 5 in Pony

    #--------------- antelope ----------------------------------------------------------------------

    #--------------- llama ----------------------------------------------------------------------
