from train.train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="captain_steel",
        base_numeric_id=21650,
        name="Captain Steel",
        subrole="branch_freight",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 1450,
        },
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        random_reverse=True,
        gen=4,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit", weight=70, vehicle_length=6, spriterow_num=0
    )

    model_def.define_description("""Imported job. No fuss, no bother.""")
    model_def.define_foamer_facts(
        """Alco S1, EMD switchers, Brush Bagnall steelworks locos"""
    )

    result.append(model_def)

    return result
