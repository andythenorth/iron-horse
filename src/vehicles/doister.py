from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="doister",
        base_numeric_id=280,
        name="0-8-0 Tiny",
        role="freight",
        role_child_branch_num=-2,
        power_by_power_source={
            "STEAM": 1250,
        },
        tractive_effort_coefficient=0.2,
        fixed_run_cost_points=140,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=2,
        intro_year_offset=10,  # introduce later than gen epoch by design
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=74, vehicle_length=5, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=24, vehicle_length=3, spriterow_num=1
    )

    consist.description = """If we do each thing calmly and carefully we will get it done quicker and with much less fuss."""
    # I don't like the name Doister, find an alternative
    # blirty?
    # is an 0=8-0 the obvious choice here?
    # https://en.wikipedia.org/wiki/LNWR_Class_G
    # https://www.lner.info/locos/Q/q1q2q3.php
    # https://www.lner.info/locos/Q/q5.php
    # https://www.lner.info/locos/Q/q6.php
    # https://www.lner.info/locos/Q/q10.php
    consist.foamer_facts = """"""

    return consist
