from train import PassengerLuxuryConsist, Wagon


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = PassengerLuxuryConsist(roster='pony',
                                     base_numeric_id=2250,
                                     gen=1,
                                     subtype='A')

    consist.add_unit(type=Wagon,
                     capacity=25,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = PassengerLuxuryConsist(roster='pony',
                                     base_numeric_id=2260,
                                     gen=2,
                                     subtype='A')

    consist.add_unit(type=Wagon,
                     capacity=40,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = PassengerLuxuryConsist(roster='pony',
                                     base_numeric_id=2270,
                                     gen=3,
                                     subtype='A')

    consist.add_unit(type=Wagon,
                     capacity=40,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = PassengerLuxuryConsist(roster='pony',
                                     base_numeric_id=3120,
                                     gen=4,
                                     subtype='A')

    consist.add_unit(type=Wagon,
                     capacity=40,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = PassengerLuxuryConsist(roster='pony',
                                     base_numeric_id=3130,
                                     gen=5,
                                     subtype='A')

    consist.add_unit(type=Wagon,
                     capacity=40,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)

    # no gen 6 for brit roster, max speed reached for engines

    #--------------- llama ----------------------------------------------------------------------

    #--------------- antelope ----------------------------------------------------------------------
