from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_def = ModelTypeFactory(
        class_name="EngineConsist",
        id="springburn",
        base_numeric_id=10830,
        name="Springburn",
        power_by_power_source={
            "DIESEL": 1200,
        },
        intro_year=1950,
    )

    model_def.define_unit(
        class_name="DieselEngineUnit", weight=80, vehicle_length=6, spriterow_num=0
    )

    result.append(model_def)

    return result
