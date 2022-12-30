from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="braf",
        base_numeric_id=0,
        name="2-6-0 Braf",  # Welsh for "fine, nice, pleasant" https://omniglot.com/language/weather/welsh.htm
        role="freight",
        role_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1250,
        },
        tractive_effort_coefficient=0.24,
        gen=2,
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=68, vehicle_length=5, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=30, vehicle_length=3, spriterow_num=1
    )

    consist.description = """Solid little number these. No bother."""
    consist.foamer_facts = """GWR 4300 Class, LBSCR K Class"""

    return consist
