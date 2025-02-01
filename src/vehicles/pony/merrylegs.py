from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="merrylegs",
        base_numeric_id=21310,
        name="2-6-2 Merrylegs",
        subrole="branch_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 650,
        },
        tractive_effort_coefficient=0.2,
        fixed_run_cost_points=120,  # substantial cost bonus so it can make money
        random_reverse=True,
        gen=2,
        caboose_family="gwr_1",
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="SteamEngineUnit", weight=49, vehicle_length=6, spriterow_num=0
    )

    consist_factory.add_description(
        """Larks were getting a bit past it.  These are right well balanced."""
    )
    consist_factory.add_foamer_facts("""GWR 4500 Class <i>Prairie Tank</i>""")

    return consist_factory
