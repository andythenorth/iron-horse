from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="lynx",
        base_numeric_id=15770,
        name="Lynx",
        role="branch_express",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1650,
        },
        random_reverse=True,
        fixed_run_cost_points=100,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=5,  # not replaced by anything (?)
        intro_year_offset=7,  # introduce later than gen epoch by design
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=72, vehicle_length=6, spriterow_num=0
    )

    consist.description = (
        """Old dog, new tricks. I've built these out of old Chinooks."""
    )
    consist.foamer_facts = """DRS Class 20/3 (re-engineered)"""

    return consist
