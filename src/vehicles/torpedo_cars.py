from train import TorpedoCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    consist = TorpedoCarConsist(roster='pony',
                              base_numeric_id=890,
                              gen=1,
                              subtype='A',
                              suppress_animated_pixel_warnings=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=5,
                     spriterow_num=0)


    consist = TorpedoCarConsist(roster='pony',
                              base_numeric_id=900,
                              gen=2,
                              subtype='A',
                              suppress_animated_pixel_warnings=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=8,
                     spriterow_num=0)


    consist = TorpedoCarConsist(roster='pony',
                              base_numeric_id=910,
                              gen=3,
                              subtype='A',
                              suppress_animated_pixel_warnings=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     spriterow_num=0)


    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     spriterow_num=0)


    consist = TorpedoCarConsist(roster='pony',
                              base_numeric_id=2670,
                              gen=4,
                              subtype='A',
                              suppress_animated_pixel_warnings=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     spriterow_num=0)


    consist = TorpedoCarConsist(roster='pony',
                              base_numeric_id=2160,
                              gen=5,
                              subtype='A',
                              suppress_animated_pixel_warnings=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     spriterow_num=0)
