# deprecated
from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="decapod",
        base_numeric_id=26080,
        name="0-10-0 Decapod",
        subrole="branch_express",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 650,
        },
        gen=2,
        intro_year_offset=7,  # let's be a little bit later for this one
        tractive_effort_coefficient=0.2,
        fixed_run_cost_points=120,  # substantial cost bonus so it can make money
        random_reverse=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="SteamEngineUnit", weight=54, vehicle_length=6, spriterow_num=0
    )

    consist_factory.add_description(
        """Don't know what they were thinking, but they asked me to build it. Well, it's done."""
    )
    consist_factory.add_foamer_facts("""GER Class A55 <i>Decapod</i>""")

    return consist_factory
