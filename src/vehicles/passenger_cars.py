from train import PassengerCarConsist, Wagon


def main():
    #--------------- pony NG----------------------------------------------------------------------
    consist = PassengerCarConsist(roster='pony',
                               base_numeric_id=770,
                               gen=1,
                               subtype='A',
                               track_type='NG')

    consist.add_unit(type=Wagon,
                     capacity=25,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)
    #--------------- pony ----------------------------------------------------------------------

    consist = PassengerCarConsist(roster='pony',
                               base_numeric_id=740,
                               gen=1,
                               subtype='A')

    consist.add_unit(type=Wagon,
                     capacity=25,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = PassengerCarConsist(roster='pony',
                               base_numeric_id=750,
                               gen=2,
                               subtype='A')

    consist.add_unit(type=Wagon,
                     capacity=40,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = PassengerCarConsist(roster='pony',
                               base_numeric_id=760,
                               gen=3,
                               subtype='A')

    consist.add_unit(type=Wagon,
                     capacity=40,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = PassengerCarConsist(roster='pony',
                               base_numeric_id=3110,
                               gen=4,
                               subtype='A')

    consist.add_unit(type=Wagon,
                     capacity=50,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = PassengerCarConsist(roster='pony',
                               base_numeric_id=3100,
                               gen=5,
                               subtype='A')

    consist.add_unit(type=Wagon,
                     capacity=50,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)
    # no gen 6 for brit roster, max speed reached for engines

    #--------------- llama ----------------------------------------------------------------------
    consist = PassengerCarConsist(roster='llama',
                               base_numeric_id=780,
                               gen=1,
                               subtype='A')

    consist.add_unit(type=Wagon,
                     capacity=40,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = PassengerCarConsist(roster='llama',
                               base_numeric_id=790,
                               gen=2,
                               subtype='A')

    consist.add_unit(type=Wagon,
                     capacity=50,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = PassengerCarConsist(roster='llama',
                               base_numeric_id=800,
                               gen=3,
                               subtype='A')

    consist.add_unit(type=Wagon,
                     capacity=60,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = PassengerCarConsist(roster='llama',
                               base_numeric_id=810,
                               gen=1,
                               subtype='A',
                               track_type='NG')

    consist.add_unit(type=Wagon,
                     capacity=30,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = PassengerCarConsist(roster='llama',
                               base_numeric_id=1350,
                               gen=2,
                               subtype='A',
                               track_type='NG')

    consist.add_unit(type=Wagon,
                     capacity=40,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = PassengerCarConsist(roster='llama',
                               base_numeric_id=1370,
                               gen=3,
                               subtype='A',
                               track_type='NG')

    consist.add_unit(type=Wagon,
                     capacity=50,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    #--------------- antelope ----------------------------------------------------------------------
    consist = PassengerCarConsist(roster='antelope',
                               base_numeric_id=1580,
                               gen=1,
                               subtype='A')

    consist.add_unit(type=Wagon,
                     capacity=55,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = PassengerCarConsist(roster='antelope',
                               base_numeric_id=1560,
                               gen=2,
                               subtype='A')

    consist.add_unit(type=Wagon,
                     capacity=80,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = PassengerCarConsist(roster='antelope',
                               base_numeric_id=2130,
                               gen=1,
                               subtype='A',
                               track_type='NG')

    consist.add_unit(type=Wagon,
                     capacity=20,
                     vehicle_length=5)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = PassengerCarConsist(roster='antelope',
                               base_numeric_id=1940,
                               gen=2,
                               subtype='A',
                               track_type='NG')

    consist.add_unit(type=Wagon,
                     capacity=30,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)
