from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="cringle",
        base_numeric_id=24480,
        name="Cringle",
        subrole="metro",
        subrole_child_branch_num=-1,
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

    consist_factory.add_unit(
        class_name="MetroUnit", weight=48, vehicle_length=8, spriterow_num=0
    )

    consist_factory.description = (
        """Engines stop running, do I have no fear?"""
    )
    consist_factory.foamer_facts = """London Underground battery-electric locos"""

    return consist_factory
