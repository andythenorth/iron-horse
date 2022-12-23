from train import PassengerHSTCabEngineConsist, DieselEngineUnit


def main(roster_id):
    consist = PassengerHSTCabEngineConsist(
        roster_id=roster_id,
        id="scorcher",
        base_numeric_id=12360,
        name="Scorcher HST",
        role="hst",  # quite a specific role, may or may not scale to other rosters
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 5850,
        },
        intro_year_offset=-10,  # let's be a little bit earlier for this one - keep match to HST coaches
        gen=6,
        lgv_capable=True,  # for lolz
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=70,
        vehicle_length=8,
        effect_offsets=[(0, 1), (0, -1)],  # double the smoke eh?
        spriterow_num=0,
        tail_light="hst_32px_1",
    )

    consist.description = """Power is of the essence. Faster is everything."""
    consist.foamer_facts = (
        """BR Class 43 (High Speed Train), life-extended with new primer mover"""
    )

    return consist
