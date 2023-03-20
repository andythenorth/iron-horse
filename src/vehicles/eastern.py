from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="eastern",
        base_numeric_id=280,
        name="0-8-0 Eastern",
        role="freight",
        role_child_branch_num=-2,
        power_by_power_source={
            "STEAM": 1250,
        },
        tractive_effort_coefficient=0.27,
        gen=2,
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=70, vehicle_length=5, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=30, vehicle_length=3, spriterow_num=1
    )

    consist.description = """If we do each thing calmly and carefully we will get it done quicker and with much less fuss."""
    # https://www.lner.info/locos/Q/q1q2q3.php
    # https://www.lner.info/locos/Q/q5.php
    # https://www.lner.info/locos/Q/q6.php
    # https://www.lner.info/locos/Q/q10.php
    consist.foamer_facts = """"""

    return consist
