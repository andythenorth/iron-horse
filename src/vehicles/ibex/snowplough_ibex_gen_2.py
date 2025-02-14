from train.train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SnowploughEngineConsist",
        base_id="snowplough_ibex_gen_2",
        base_numeric_id=9020,
        name="Snowplough",
        gen=2,
        speed=75,
        sprites_complete=False,
    )

    model_def.add_unit_def(class_name="SnowploughUnit", weight=50, vehicle_length=4)

    model_def.define_description("""""")
    model_def.define_foamer_facts("""""")

    result.append(model_def)

    return result
