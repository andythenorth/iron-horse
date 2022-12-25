from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="gronk",
        base_numeric_id=13010,
        name="Gronk",
        role="gronk!",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 400,
        },
        speed=35,
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        fixed_run_cost_points=100,  # substantial cost bonus so it can make money
        random_reverse=True,
        gen=4,
        intro_year_offset=-9,  # introduce much earlier than gen epoch by design
        vehicle_life=60,  # extended vehicle life for all gronks eh
        additional_liveries=["BANGER_BLUE", "DBSCHENKER"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=55, vehicle_length=4, spriterow_num=0
    )

    consist.description = """The universal shunter.  Goes everywhere&hellip;slowly."""
    consist.foamer_facts = """BR Class 08/09"""

    return consist
