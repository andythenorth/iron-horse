from train import PassengerEngineCabControlCarConsist, CabControlPaxCarUnit


def main(roster_id):
    consist = PassengerEngineCabControlCarConsist(
        roster_id=roster_id,
        id="driving_cab_passenger_pony_gen_4",
        base_numeric_id=14430,
        name="Driving Trailer",
        gen=4,
        intro_date_offset=16,  # a lot later, very short lived, replaced by gen 5 quickly
        sprites_complete=True,
    )

    consist.add_unit(type=CabControlPaxCarUnit, weight=32, chassis="railcar_32px")

    consist.description = """Front or back of a train, up to you. Supplies hotel power for the coaches, so your main loco has more power for traction. Clever idea we had eh?"""
    consist.foamer_facts = (
        """BR MK2 Driving Brake Standard Open (DBSO) with added generator"""
    )

    return consist
