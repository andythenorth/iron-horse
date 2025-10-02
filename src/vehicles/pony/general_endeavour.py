from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="general_endeavour",
        base_numeric_id=20980,
        name="General Endeavour",
        subrole="branch_freight",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 1650,
        },
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        random_reverse=True,
        gen=5,
        liveries=["STOCK_STANDARD", "DYNAMIC_LINES", "LOWER_LINES", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=70,
        vehicle_length=6,
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """I can make a General in five minutes, but a good horse is hard to replace."""
    )
    model_def.define_foamer_facts(
        """Upgraded Alco S1, EMD switchers, Brush Bagnall steelworks locos"""
    )

    result.append(model_def)

    return result
