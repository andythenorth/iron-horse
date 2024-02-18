from train import PassengerEngineCabControlCarConsist, CabControlPaxCarUnit


def main(roster_id, **kwargs):
    consist = PassengerEngineCabControlCarConsist(
        roster_id=roster_id,
        id="driving_cab_passenger_pony_gen_5",
        base_numeric_id=14210,
        name="Driving Trailer",
        role_child_branch_num=-1,  # driving cab cars are probably jokers?
        gen=5,
        liveries="gen_5_and_6_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    consist.add_unit(type=CabControlPaxCarUnit, weight=32, chassis="railcar_32px")

    consist.description = """Front or back of a train, up to you. Supplies hotel power for the coaches, so your main loco has more power for traction. Clever idea we had eh?"""
    consist.foamer_facts = (
        """BR MK2 Driving Brake Standard Open (DBSO) with added generator"""
    )

    return consist
