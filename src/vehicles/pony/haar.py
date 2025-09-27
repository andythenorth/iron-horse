from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="haar",
        base_numeric_id=1880,
        name="0-8-0 Haar",
        subrole="freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1500,
        },
        tractive_effort_coefficient=0.24,
        gen=3,
        liveries=["WORKHORSE", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
        weight=70,
        vehicle_length=5,
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        class_name="SteamEngineTenderUnit",
        weight=40,
        vehicle_length=3,
        rel_spriterow_index=1,
    )

    model_def.define_description(
        """This is right ugly, but the shed likes them. Easy to maintain. They'll do."""
    )
    model_def.define_foamer_facts("""SR Q1 Class, LMS Class 7F""")

    result.append(model_def)

    return result
