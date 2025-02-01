from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="magnum_90",
        base_numeric_id=21680,
        name="Magnum 90",
        subrole="gronk",
        subrole_child_branch_num=-4,
        power_by_power_source={
            "BATTERY_HYBRID": 900,
        },
        speed=35,
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        fixed_run_cost_points=100,  # substantial cost bonus so it can make money
        random_reverse=True,
        gen=6,
        intro_year_offset=-6,  # introduce earlier than gen epoch by design
        extended_vehicle_life=True,  # extended vehicle life for all gronks eh
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="BatteryHybridEngineUnit",
        weight=90,
        vehicle_length=8,
        spriterow_num=0,
    )

    consist_factory.add_description("""Even Gronks don't last forever.""")
    consist_factory.add_foamer_facts("""Clayton CBD90""")

    result.append(consist_factory)

    return result
