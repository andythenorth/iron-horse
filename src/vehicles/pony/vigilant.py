from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="vigilant",
        base_numeric_id=4870,
        name="2-8-0 Vigilant",
        subrole="super_heavy_freight",
        subrole_child_branch_num=1,  # child branch 1 empty, for tech tree drawing reasons (blackthorn and quietus in branch -1)
        power_by_power_source={
            "STEAM": 1850,
        },
        tractive_effort_coefficient=0.32,
        fixed_run_cost_points=245,  # cost malus, early heavy freight engines are too cheap to run relative to smaller engines
        gen=2,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH", "BANGER_BLUE", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="SteamEngineUnit", weight=92, vehicle_length=6, spriterow_num=0
    )

    consist_factory.define_unit(
        class_name="SteamEngineTenderUnit", weight=40, vehicle_length=4, spriterow_num=1
    )

    consist_factory.define_description(
        """It's a big engine, it cost a lot of brass, get it to work."""
    )
    consist_factory.define_foamer_facts("""GCR Class 8K / ROD 2-8-0, GWR 2800 Class""")

    result.append(consist_factory)

    return result
