from train import EngineConsist, SteamEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="fireball",
        base_numeric_id=23990,
        name="0-6-0 Fireball",
        role="gronk!",
        role_child_branch_num=-3,
        power_by_power_source={
            "STEAM": 350,
        },
        speed=35,
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        fixed_run_cost_points=101,  # substantial cost bonus so it can make money
        random_reverse=True,
        gen=1,
        intro_year_offset=2,  # introduce later than gen epoch by design
        extended_vehicle_life=True,  # extended vehicle life for all gronks eh
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        caboose_family="gwr_1",
        sprites_complete=True,
    )

    consist.add_unit(type=SteamEngineUnit, weight=35, vehicle_length=4, spriterow_num=0)

    consist.description = """Your typical pint-sized workhorse."""
    consist.foamer_facts = """GWR 1366 Class pannier tanks"""

    return consist
