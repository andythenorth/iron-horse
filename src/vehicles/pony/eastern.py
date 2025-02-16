from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_type_id="eastern",
        base_numeric_id=280,
        name="0-8-0 Eastern",
        subrole="freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1250,
        },
        tractive_effort_coefficient=0.27,
        gen=2,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
        weight=70,
        vehicle_length=5,
        spriterow_num=0,
    )

    model_def.add_unit_def(
        class_name="SteamEngineTenderUnit", weight=30, vehicle_length=3, spriterow_num=1
    )

    model_def.define_description(
        """If we do each thing calmly and carefully we will get it done quicker and with much less fuss."""
    )
    model_def.define_foamer_facts("""LNER Q2 Class""")

    result.append(model_def)

    return result
