from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="carrack",
        base_numeric_id=1860,
        name="4-4-0 Carrack",
        subrole="express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1200,
        },
        tractive_effort_coefficient=0.18,
        fixed_run_cost_points=140,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=2,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        extended_vehicle_life=True,
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "BANGER_BLUE"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
        weight=60,
        vehicle_length=5,
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        class_name="SteamEngineTenderUnit",
        weight=30,
        vehicle_length=3,
        rel_spriterow_index=1,
    )

    model_def.define_description(
        """It's not the biggest, but there's nowt wrong wi this one."""
    )
    model_def.define_foamer_facts(
        """Midland Railway 483 Class, GWR <i>City</i> 3700 Class, generic 4-4-0 locomotives"""
    )

    result.append(model_def)

    return result
