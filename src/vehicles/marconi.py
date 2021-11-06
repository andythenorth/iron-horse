from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="marconi",
        base_numeric_id=6730,
        name="Marconi",
        role="branch_express",
        role_child_branch_num=-1,
        power=1650,
        random_reverse=True,
        fixed_run_cost_points=100,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=5,  # not replaced by anything (?)
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=72, vehicle_length=6, spriterow_num=0
    )

    consist.description = """."""
    consist.foamer_facts = """DRS Class 20/3"""

    return consist
