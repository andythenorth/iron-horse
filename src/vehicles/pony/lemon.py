from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="lemon",
        base_numeric_id=270,
        name="4-8-0 Lemon",
        subrole="super_heavy_freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 2400,
        },
        speed=75,  # for lolz
        tractive_effort_coefficient=0.29,
        gen=3,
        liveries=["VANILLA", "BANGER_BLUE", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
        weight=115,
        vehicle_length=8,
        effect_offsets=[(-3, 0), (-2, 0)],  # double the smoke eh?
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        class_name="SteamEngineTenderUnit",
        weight=50,
        vehicle_length=4,
        rel_spriterow_index=1,
    )

    model_def.define_description(
        """I'm not saying I'm the best engine builder in the business, but I'd be in the top one."""
    )
    model_def.define_foamer_facts(
        """proposed LMS 'Lemon 4-8-0' freight locomotive, BR Standard Class 9F"""
    )

    result.append(model_def)

    return result
