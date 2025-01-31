from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="pinhorse",
        base_numeric_id=21860,
        name="Pinhorse",
        subrole="branch_express",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 1050,  # matched to Stoat
        },
        random_reverse=True,
        pantograph_type="diamond-single",
        gen=2,
        intro_year_offset=3,  # introduce later than gen epoch by design
        fixed_run_cost_points=120,  # substantial cost bonus for balance against same-era steam engines
        extended_vehicle_life=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="ElectricEngineUnit", weight=60, vehicle_length=6, spriterow_num=0
    )

    consist_factory.description = (
        """These are bob on. For small jobs, you won't go far wrong with em."""
    )
    consist_factory.foamer_facts = """Metropolitan Railway electric locos"""

    return consist_factory
