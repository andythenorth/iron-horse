from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="EngineConsist",
        id="u28cg",
        base_numeric_id=22050,
        name="u28cg / u30gc",
        subrole="heavy_express",
        subrole_child_branch_num=-3,
        power_by_power_source={
            "DIESEL": 2800,  # nerfed to account for HEP
        },
        random_reverse=True,
        gen=4,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[],
        sprites_complete=False,
    )

    model_type_factory.define_unit(
        class_name="DieselEngineUnit",
        weight=160,
        vehicle_length=8,
    )

    model_type_factory.define_description("""""")
    model_type_factory.define_foamer_facts("""""")

    result.append(model_type_factory)

    return result
