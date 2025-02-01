from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="strongbow",
        base_numeric_id=4320,
        name="4-6-0 Strongbow",
        subrole="heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1850,  # not an exact linear progression in this tree
        },
        tractive_effort_coefficient=0.18,
        gen=3,
        fixed_run_cost_points=120,  # give a bonus so this can be a genuine mixed-traffic engine
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "SWOOSH", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="SteamEngineUnit", weight=96, vehicle_length=6, spriterow_num=0
    )

    consist_factory.add_unit(
        class_name="SteamEngineTenderUnit", weight=34, vehicle_length=4, spriterow_num=1
    )

    consist_factory.add_description(
        """Got this one off Mr. Stanier.  It'll go anywhere, do anything, for not too much brass."""
    )
    consist_factory.add_foamer_facts(
        """LMS Jubilee Class, original TTD Chaney 'Jubilee'"""
    )

    return consist_factory
