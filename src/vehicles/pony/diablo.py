from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="diablo",
        base_numeric_id=4910,
        name="2-6-0 Diablo",
        subrole="express",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 1450,
        },
        tractive_effort_coefficient=0.22,
        fixed_run_cost_points=140,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=3,
        intro_year_offset=4,  # introduce a bit later
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="SteamEngineUnit", weight=70, vehicle_length=5, spriterow_num=0
    )

    consist_factory.add_unit(
        class_name="SteamEngineTenderUnit", weight=36, vehicle_length=3, spriterow_num=1
    )

    consist_factory.description = """Right happy with the look of these."""
    consist_factory.foamer_facts = (
        """LMS <i>Hughes Crab</i>, BR Standard Class 4 2-6-0"""
    )

    return consist_factory
