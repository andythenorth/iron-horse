from train import PassengerHSTCarConsist, HSTPaxCar

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = PassengerHSTCarConsist(roster='pony',
                                     base_numeric_id=3480,
                                     gen=5,
                                     subtype='U',
                                     intro_date_offset=-10, # match to Blaze HST
                                     sprites_complete=True)

    consist.add_unit(type=HSTPaxCar,
                     chassis='4_axle_solid_express_32px')


    consist = PassengerHSTCarConsist(roster='pony',
                                     base_numeric_id=3490,
                                     gen=6,
                                     subtype='U',
                                     intro_date_offset=-10, # match to Scorcher HST
                                     sprites_complete=False)

    consist.add_unit(type=HSTPaxCar,
                     chassis='4_axle_solid_express_32px')
