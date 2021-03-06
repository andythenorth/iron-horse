from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="wyvern",
        base_numeric_id=2950,
        name="Wyvern",
        role="heavy_express",
        role_child_branch_num=1,
        power=2200,  # not an exact linear progression in this tree
        random_reverse=True,
        gen=4,
        intro_date_offset=-6,  # let's not have everything turn up in 1960
        fixed_run_cost_points=30,  # give a bonus so this can be a genuine mixed-traffic engine
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=130, vehicle_length=8, spriterow_num=0
    )

    consist.description = """Turn the key and it goes.  It's right heavy for what it is, but you can't argue with progress."""
    consist.foamer_facts = """BR Class 40 and Class 44/45/46 <i>Peaks</i>"""

    return consist
