from train import MailEngineDrivingCabConsist, DrivingCabUnit

def main(roster):
    consist = MailEngineDrivingCabConsist(roster=roster,
                                          id='cabbage_1',
                                          base_numeric_id=3980,
                                          name='Driving Van Trailer',
                                          gen=5,
                                          joker=True,
                                          sprites_complete=False)

    consist.add_unit(type=DrivingCabUnit,
                     weight=30,
                     chassis='railcar_32px')

    return consist
