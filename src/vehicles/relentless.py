from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="relentless",
        base_numeric_id=13440,
        name="Relentless",
        role="super_heavy_express",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 4250,  # slightly more than standard progression, to enable higher speed to be reach quickly
        },
        random_reverse=True,
        gen=6,
        fixed_run_cost_points=300,  # give a small malus to this one (balancing eh?)
        # banger blue?
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=95, vehicle_length=8, spriterow_num=0
    )

    consist.description = """Solid piece of kit these."""
    consist.foamer_facts = (
        """Newag Griffin, Bombardier Traxx 2, Stadler Euro 4001, Siemens EuroRunner"""
    )

    return consist
