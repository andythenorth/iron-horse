from train import EngineConsist, DieselEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="progress",
        base_numeric_id=16860,
        name="Progress",
        role="gronk!",
        role_child_branch_num=-3,
        power_by_power_source={
            "DIESEL": 400,
        },
        speed=35,
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        fixed_run_cost_points=100,  # substantial cost bonus so it can make money
        random_reverse=True,
        gen=4,
        extended_vehicle_life=True,  # extended vehicle life for all gronks eh
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=48, vehicle_length=4, spriterow_num=0
    )

    consist.description = """Punchy little number."""
    consist.foamer_facts = """GEC <i>Stephenson</i> industrial shunters, BR Class 07"""

    return consist
