from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="yak",
        base_numeric_id=21260,
        name="0-8-2 Yak",
        subrole="branch_freight",
        subrole_child_branch_num=-3,
        power_by_power_source={
            "STEAM": 1000,
        },
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        random_reverse=True,
        gen=3,
        intro_year_offset=0,
        liveries=["WORKHORSE", "FREIGHT_BLACK", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="SteamEnginePoweredUnit",
        weight=70,
        vehicle_length=6,
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """We ought to do good to others as simply as a horse runs."""
    )
    model_def.define_foamer_facts("""LNER Thompson Q1 Class tank engine""")

    result.append(model_def)

    return result
