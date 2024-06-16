from train import EngineConsist, MetroUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="cringle",
        base_numeric_id=24480,
        name="Cringle",
        role="metro",
        role_child_branch_num=-1,
        power_by_power_source={
            "METRO": 900,
        },
        random_reverse=True,
        gen=2,
        fixed_run_cost_points=120,  # substantial cost bonus for balance against same-era steam engines
        extended_vehicle_life=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=MetroUnit, weight=48, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """Engines stop running, do I have no fear?"""
    )
    consist.foamer_facts = """London Underground battery-electric locos"""

    return consist
