from train import ReeferConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    # no gen 1 reefer - straight to gen 2

    consist = ReeferConsist(roster='pony',
                            base_numeric_id=730,
                            gen=2,
                            subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = ReeferConsist(roster='pony',
                            base_numeric_id=720,
                            gen=3,
                            subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = ReeferConsist(roster='pony',
                            base_numeric_id=2560,
                            gen=4,
                            subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = ReeferConsist(roster='pony',
                            base_numeric_id=2590,
                            gen=4,
                            subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = ReeferConsist(roster='pony',
                            base_numeric_id=2570,
                            gen=5,
                            subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = ReeferConsist(roster='pony',
                            base_numeric_id=2580,
                            gen=5,
                            subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    #--------------- llama ----------------------------------------------------------------------
    consist = ReeferConsist(roster='llama',
                            base_numeric_id=1390,
                            gen=1,
                            subtype='A',
                            speedy=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    # no gen 2 reefers - straight to gen 3
    consist = ReeferConsist(roster='llama',
                            base_numeric_id=1400,
                            gen=3,
                            subtype='A',
                            speedy=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = ReeferConsist(roster='llama',
                            base_numeric_id=1410,
                            gen=1,
                            subtype='A',
                            speedy=True,
                            track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    # no gen 2 reefers - straight to gen 3
    consist = ReeferConsist(roster='llama',
                            base_numeric_id=1420,
                            gen=3,
                            subtype='A',
                            speedy=True,
                            track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    #--------------- antelope ----------------------------------------------------------------------
    consist = ReeferConsist(roster='antelope',
                            base_numeric_id=1570,
                            gen=1,
                            subtype='A',
                            speedy=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = ReeferConsist(roster='antelope',
                            base_numeric_id=1900,
                            gen=1,
                            subtype='A',
                            speedy=True,
                            track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])
