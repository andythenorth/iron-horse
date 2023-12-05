from train import PassengerHSTCabEngineConsist, DieselEngineUnit


def main(roster_id):
    consist = PassengerHSTCabEngineConsist(
        roster_id=roster_id,
        id="scorcher",
        base_numeric_id=12360,
        name="Scorcher HST",
        role="hst",  # quite a specific role, may or may not scale to other rosters
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 5500,
            "AC": 7200,
        },
        intro_year_offset=-8,  # let's be a little bit earlier for this one - keep match to HST coaches
        gen=6,
        lgv_capable=True,  # for lolz
        #note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH"],
        sprites_complete=True,
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
        """IEP THING CLASS 800 CABBAGE"""
    )

    return consist
