from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="braf",
        base_numeric_id=0,
        name="2-6-0 Braf",  # Welsh for "fine, nice, pleasant" https://omniglot.com/language/weather/welsh.htm
        role="freight",
        role_child_branch_num=2,
        power_by_power_source={
            "STEAM": 1250,
        },
        tractive_effort_coefficient=0.24,
        gen=2,
        intro_year_offset=5,  # introduce later than gen epoch by design
        additional_liveries=["FREIGHT_BLACK"],
        sprites_complete=True,
    )

    consist.add_unit(type=SteamEngineUnit, weight=65, vehicle_length=5, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=29, vehicle_length=3, spriterow_num=1
    )

    consist.description = """Solid little number these. No bother."""
    consist.foamer_facts = """GWR 4300 Class, LBSCR K Class"""

    return consist
