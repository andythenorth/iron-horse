from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="SnowploughEngineConsist",
        id="snowplough_pony_gen_2",
        base_numeric_id=25130,
        name="Snowplough",
        gen=2,
        speed=75,
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="SnowploughUnit", weight=50, vehicle_length=4
    )

    model_type_factory.define_description(
        """Does it ever snow here?  I wouldn't say, but these are waiting just in case."""
    )
    model_type_factory.define_foamer_facts("""LNER / BR Independent Snowploughs""")

    result.append(model_type_factory)

    return result
