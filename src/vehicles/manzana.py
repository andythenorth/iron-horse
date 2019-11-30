from train import PassengerEngineConsist, MetroUnit


def main(roster_id):
    consist = PassengerEngineConsist(roster_id=roster_id,
                                     id='manzana',
                                     base_numeric_id=1480,
                                     name='Manzana',
                                     power=900,
                                     intro_date=1950)

    # should be 4 units not 2
    consist.add_unit(type=MetroUnit,
                     weight=40,
                     vehicle_length=8,
                     capacity=160,
                     spriterow_num=0)

    consist.add_unit(type=MetroUnit,
                     weight=40,
                     vehicle_length=8,
                     capacity=160,
                     spriterow_num=1)

    return consist
