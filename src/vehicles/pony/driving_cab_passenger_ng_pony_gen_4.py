from train import PassengerEngineCabControlCarConsist, CabControlPaxCarUnit


def main(roster_id, **kwargs):
    consist = PassengerEngineCabControlCarConsist(
        roster_id=roster_id,
        id="driving_cab_passenger_ng_pony_gen_4",
        base_numeric_id=23260,
        name="Driving Trailer",
        role_child_branch_num=-1,  # driving cab cars are probably jokers?
        base_track_type_name="NG",
        gen=4,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        sprites_complete=True,
    )

    consist.add_unit(type=CabControlPaxCarUnit, weight=32, chassis="4_axle_ng_32px")

    consist.description = (
        """Now, a driving cab for the smaller trains. But not for goats."""
    )
    consist.foamer_facts = (
        """KiwiRail SRV driving cab conversion of British Rail MK2 carriage"""
    )

    return consist
