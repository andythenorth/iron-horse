from train import PassengerEngineCabControlCarConsist, CabControlPaxCarUnit


def main(roster_id):
    consist = PassengerEngineCabControlCarConsist(
        roster_id=roster_id,
        id="driving_cab_passenger_pony_gen_6",
        base_numeric_id=5180,
        name="Driving Trailer",
        gen=6,
        sprites_complete=True,
    )

    consist.add_unit(type=CabControlPaxCarUnit, weight=32, chassis="railcar_32px")

    consist.description = """Front or back of a train, up to you. Supplies hotel power for the coaches, so your main loco has more power for traction. Clever idea we had eh?"""
    consist.foamer_facts = """BR MK2 DBSO with added generator"""

    return consist
