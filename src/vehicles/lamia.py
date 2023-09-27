from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="lamia",
        base_numeric_id=13920,
        name="0-6-0 Lamia",  # the name is the Basque mythical creature, not the Greek https://en.wikipedia.org/wiki/Lamia_(Basque_mythology)
        role="gronk!",
        role_child_branch_num=-2,
        replacement_consist_id="chuggypig",  # this Joker ends with Gronk
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
        extended_vehicle_life=True, # extended vehicle life for all gronks eh
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist.add_unit(type=SteamEngineUnit, weight=35, vehicle_length=4, spriterow_num=0)

    consist.description = """Nice little engine this one."""
    consist.foamer_facts = """Bagnall saddle tanks"""

    return consist
