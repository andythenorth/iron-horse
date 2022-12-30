from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="carrack",
        base_numeric_id=1040,
        name="4-4-0 Carrack",
        role="express",
        role_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1150,
        },
        tractive_effort_coefficient=0.18,
        gen=2,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=60, vehicle_length=5, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=30, vehicle_length=3, spriterow_num=1
    )

    consist.description = (
        """It's not the biggest, but there's nowt wrong wi this one."""
    )
    consist.foamer_facts = """Midland Railway 483 Class, GWR <i>City</i> 3700 Class, generic 4-4-0 locomotives"""

    return consist
