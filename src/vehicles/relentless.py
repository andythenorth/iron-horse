from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="relentless",
        base_numeric_id=13440,
        name="Relentless",
        role="super_heavy_express",
        role_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 4200,
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.355,
        random_reverse=True,
        gen=6,
        fixed_run_cost_points=190,  # run cost nerf as light weight throws the cost too cheap
        #note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=112, vehicle_length=8, spriterow_num=0
    )

    consist.description = """Solid piece of kit these."""
    consist.foamer_facts = (
        """Newag Griffin, Bombardier Traxx 2, Stadler Euro 4001, Siemens EuroRunner"""
    )

    return consist
