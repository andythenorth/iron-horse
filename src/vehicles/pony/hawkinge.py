from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        id="hawkinge",
        base_numeric_id=6410,
        name="4-8-2 Hawkinge",
        subrole="super_heavy_express",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "STEAM": 2350,
        },
        tractive_effort_coefficient=0.25,
        fixed_run_cost_points=120,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=3,
        intro_year_offset=5,  # introduce later than gen epoch by design
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="SteamEngineUnit",
        weight=124,
        vehicle_length=8,
        effect_offsets=[(-3, 0), (-2, 0)],  # double the smoke eh?
        spriterow_num=0,
    )

    model_def.add_unit(
        class_name="SteamEngineTenderUnit", weight=32, vehicle_length=4, spriterow_num=1
    )

    model_def.define_description(
        """Mr. Bulleid designed these. Do you like 'em?"""
    )
    model_def.define_foamer_facts(
        """SR Merchant Navy / West Country / Battle of Britain classes"""
    )

    result.append(model_def)

    return result
