from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="esk",
        base_numeric_id=4050,
        name="2-6-0+0-6-2 Esk",
        subrole="super_heavy_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 2400,
        },
        tractive_effort_coefficient=0.4,
        gen=3,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="SteamEngineTenderUnit", weight=60, vehicle_length=3, spriterow_num=0
    )

    consist_factory.add_unit(
        class_name="SteamEngineUnit",
        weight=60,
        vehicle_length=6,
        effect_offsets=[(-3, 0)],
        spriterow_num=1,
    )

    consist_factory.add_unit(
        class_name="SteamEngineTenderUnit", weight=60, vehicle_length=3, spriterow_num=2
    )

    consist_factory.add_description("""Well it's a big bugger isn't it.""")
    consist_factory.add_foamer_facts("""LMS Garratt""")

    return consist_factory
