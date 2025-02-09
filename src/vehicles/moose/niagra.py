from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        id="niagra",
        base_numeric_id=34880,
        name="Niagra",
        subrole="branch_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1150,
        },
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        random_reverse=True,
        gen=4,
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit", weight=70, vehicle_length=6, spriterow_num=0
    )

    model_def.define_description("""""")
    model_def.define_foamer_facts("""""")

    result.append(model_def)

    return result
