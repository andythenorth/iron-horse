from train import MailEngineDrivingCabConsist, DrivingCabUnit

def main(roster_id):
    consist = MailEngineDrivingCabConsist(roster_id=roster_id,
                                          id='driving_cab_pony_gen_6',
                                          base_numeric_id=3990,
                                          name='Driving Van Trailer',
                                          gen=6,
                                          joker=True,
                                          sprites_complete=True)

    consist.add_unit(type=DrivingCabUnit,
                     weight=34,
                     chassis='railcar_32px')

    return consist
