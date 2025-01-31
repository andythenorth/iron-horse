from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="relentless",
        base_numeric_id=21460,
        name="Relentless",
        subrole="super_heavy_express",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 4200,
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.355,
        random_reverse=True,
        gen=6,
        fixed_run_cost_points=190,  # run cost nerf as light weight throws the cost too cheap
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit", weight=112, vehicle_length=8, spriterow_num=0
    )

    consist_factory.description = """Solid piece of kit these."""
    consist_factory.foamer_facts = (
        """Newag Griffin, Bombardier Traxx 2, Stadler Euro 4001, Siemens EuroRunner"""
    )

    return consist_factory
