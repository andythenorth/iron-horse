from train import PassengerEngineCabControlCarConsist, CabControlPaxCarUnit


def main(roster_id):
    consist = PassengerEngineCabControlCarConsist(
        roster_id=roster_id,
        id="driving_cab_high_speed_passenger_pony_gen_6",
        base_numeric_id=9200,
        name="High Speed Driving Trailer",
        role_child_branch_num=-3,  # driving cab cars are probably jokers?
        gen=6,
        lgv_capable=True,  # for lolz
        sprites_complete=True,
    )

    consist.add_unit(type=CabControlPaxCarUnit, weight=32, chassis="railcar_32px")

    consist.description = """Front or back of a train, up to you. Supplies hotel power for the coaches, so your main loco has more power for traction. Clever idea we had eh?"""
    consist.foamer_facts = """CAF MK5A Driving Trailer (DT) with added generator"""

    return consist
