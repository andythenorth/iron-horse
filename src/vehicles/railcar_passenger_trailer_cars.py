from train import PassengerRailcarTrailerCarConsist, PaxRailcarTrailerCar


def main():
    #--------------- pony NG----------------------------------------------------------------------

    consist = PassengerRailcarTrailerCarConsist(roster_id='pony',
                                                base_numeric_id=990,
                                                gen=3,
                                                subtype='U',
                                                base_track_type='NG',
                                                sprites_complete=True)

    consist.add_unit(type=PaxRailcarTrailerCar,
                     chassis='4_axle_ng_24px',
                     tail_light='railcar_24px_1')


    consist = PassengerRailcarTrailerCarConsist(roster_id='pony',
                                                base_numeric_id=4470,
                                                gen=4,
                                                subtype='U',
                                                base_track_type='NG',
                                                sprites_complete=True)

    consist.add_unit(type=PaxRailcarTrailerCar,
                     chassis='4_axle_ng_24px',
                     tail_light='railcar_24px_1')


    #--------------- pony ----------------------------------------------------------------------

    # gen 3 could be added but needs the engine grilles replacing with pax car pixels

    consist = PassengerRailcarTrailerCarConsist(roster_id='pony',
                                                base_numeric_id=2940,
                                                gen=4,
                                                subtype='U',
                                                intro_date_offset=-5,  # introduce early by design
                                                sprites_complete=True)

    consist.add_unit(type=PaxRailcarTrailerCar,
                     chassis='4_axle_solid_express_32px',
                     tail_light='railcar_32px_2')


    consist = PassengerRailcarTrailerCarConsist(roster_id='pony',
                                                base_numeric_id=2910,
                                                gen=5,
                                                subtype='U',
                                                intro_date_offset=-5,  # introduce early by design
                                                sprites_complete=True)

    consist.add_unit(type=PaxRailcarTrailerCar,
                     chassis='4_axle_solid_express_32px',
                     tail_light='railcar_32px_3')


    consist = PassengerRailcarTrailerCarConsist(roster_id='pony',
                                                base_numeric_id=2050,
                                                gen=6,
                                                subtype='U',
                                                intro_date_offset=-5,  # introduce early by design
                                                sprites_complete=True)

    consist.add_unit(type=PaxRailcarTrailerCar,
                     chassis='4_axle_solid_express_32px',
                     tail_light='railcar_32px_2')
