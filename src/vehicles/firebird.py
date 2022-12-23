from train import PassengerHSTCabEngineConsist, DieselEngineUnit


def main(roster_id):
    consist = PassengerHSTCabEngineConsist(
        roster_id=roster_id,
        id="firebird",
        base_numeric_id=12870,
        name="Firebird",
        role="hst",  # quite a specific role, may or may not scale to other rosters
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 3300,  # it's the Deltic that never was!  It's OP, but eh, it's just cartoon trains.
        },
        gen=4,
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=68,
        vehicle_length=8,
        capacity=16,
        effect_offsets=[(0, 1), (0, -1)],  # double the smoke eh?
        spriterow_num=0,
        tail_light="hst_32px_1",
    )

    consist.description = """The Train of Today."""
    consist.foamer_facts = """BR <i>Blue Pullman</i>"""

    return consist
