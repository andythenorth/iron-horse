from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        id="sdp40f",
        base_numeric_id=22040,
        name="sdp40f",
        subrole="heavy_express",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 2800,  # nerfed to account for HEP
        },
        random_reverse=True,
        gen=4,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[],
        sprites_complete=False,
    )

    model_def.add_unit(
        class_name="DieselEngineUnit",
        weight=160,
        vehicle_length=8,
    )

    model_def.define_description("""""")
    model_def.define_foamer_facts("""""")

    result.append(model_def)

    return result
