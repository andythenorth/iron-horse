from train import EngineConsist, DieselEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="chuggypig",
        base_numeric_id=21660,
        name="Chuggypig",
        role="gronk!",
        role_child_branch_num=-2,
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

    consist.description = """No prizes for speed, but it gets a job done."""
    consist.foamer_facts = """Thomas Hill <i>Steelman</i>, miscellaneous industrial diesel shunters"""

    return consist
