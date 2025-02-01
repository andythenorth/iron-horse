from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="mainstay",
        base_numeric_id=6360,
        name="2-8-0 Mainstay",
        subrole="heavy_freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1850,
        },
        speed=60,
        tractive_effort_coefficient=0.23,
        gen=3,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="SteamEngineUnit", weight=96, vehicle_length=6, spriterow_num=0
    )

    consist_factory.add_unit(
        class_name="SteamEngineTenderUnit", weight=50, vehicle_length=4, spriterow_num=1
    )

    consist_factory.description = """Bombproof."""
    consist_factory.foamer_facts = """WD Austerity 2-8-0, USRA S160 Class 2-8-0"""

    return consist_factory
