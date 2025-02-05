from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="SnowploughEngineConsist",
        id="snowplough_moose_gen_2",
        base_numeric_id=34890,
        name="Snowplough",
        gen=2,
        speed=75,
        sprites_complete=False,
    )

    model_type_factory.define_unit(
        class_name="SnowploughUnit", weight=50, vehicle_length=4
    )

    model_type_factory.define_description("""MOOSE.""")
    model_type_factory.define_foamer_facts("""MOOSE""")

    result.append(model_type_factory)

    return result
