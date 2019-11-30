from train import MailEngineDrivingCabConsist, DrivingCabUnit

def main(roster_id):
    consist = MailEngineDrivingCabConsist(roster_id=roster_id,
                                          id='driving_cab_pony_gen_5',
                                          base_numeric_id=3980,
                                          name='Driving Van Trailer',
                                          gen=5,
                                          joker=True,
                                          sprites_complete=True)

    consist.add_unit(type=DrivingCabUnit,
                     weight=32,
                     chassis='railcar_32px')

    return consist
