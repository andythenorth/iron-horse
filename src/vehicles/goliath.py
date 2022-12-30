from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="goliath",
        base_numeric_id=10760,
        name="Goliath",
        role="branch_freight",
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 1300,  # progression drops a bit on hp/speed ratio from previous gen, but it's fine, this is for low-end roles
        },
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        random_reverse=True,
        gen=5,
        intro_year_offset=2,  # introduce later than gen epoch by design
        caboose_family="railfreight_2",
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=71, vehicle_length=6, spriterow_num=0
    )

    consist.description = """It gets the job done either way."""
    consist.foamer_facts = (
        """YEC <i>Janus</i>, Corus <i>Trojan</i>, Corus Hunslet Bo-bo"""
    )

    return consist
