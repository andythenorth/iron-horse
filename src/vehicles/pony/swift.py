from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="swift",
        base_numeric_id=230,
        name="4-4-2 Swift",
        subrole="heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1550,
        },
        tractive_effort_coefficient=0.18,
        gen=2,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="SteamEngineUnit", weight=80, vehicle_length=6, spriterow_num=0
    )

    consist_factory.add_unit(
        class_name="SteamEngineTenderUnit", weight=35, vehicle_length=4, spriterow_num=1
    )

    consist_factory.description = """Eh it's the right big engine I said they needed. Mr. Raven helped me out a treat with this one."""
    consist_factory.foamer_facts = """GNR Class C1, Class C2 <i>Klondike</i>"""

    return consist_factory
