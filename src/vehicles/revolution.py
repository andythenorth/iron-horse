from train import EngineConsist, ElectroDieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="revolution",
        base_numeric_id=12540,
        name="Revolution",
        role="heavy_express",
        role_child_branch_num=1,  # in the diesel branch, not electric
        power_by_power_source={
            "DIESEL": 2950,
            "AC": 4200,
        },  # compared to IRL, there is more diesel power and less electric, follows Fury line 600hp progresion steps
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=6,
        fixed_run_cost_points=280,  # run cost nerf for bi-mode flexibility + high el-power
        intro_year_offset=-2,  # introduce earlier than gen epoch by design
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectroDieselEngineUnit, weight=95, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """Bobby-dazzlers these are. How they fit it all in amazes me."""
    )
    consist.foamer_facts = """Vossloh Euro Dual (DRS Class 88, ROG Class 93)"""

    return consist
