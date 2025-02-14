from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="sd45",
        base_numeric_id=22020,
        name="SD45",
        subrole="super_heavy_freight",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 3600,  # first high HP diesel in this roster??
        },
        random_reverse=True,
        gen=4,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=160,
        vehicle_length=8,
    )

    model_def.define_description("""""")
    model_def.define_foamer_facts("""""")

    result.append(model_def)

    return result
