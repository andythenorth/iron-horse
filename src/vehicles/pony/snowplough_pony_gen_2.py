from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SnowploughEngine",
        model_id="snowplough_pony_gen_2",
        base_numeric_id=25130,
        name="Snowplough",
        gen=2,
        speed=75,
        liveries=["CONVENTIONAL_WISDOM"],
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="SnowploughUnit", weight=50, vehicle_length=4)

    model_def.define_description(
        """Does it ever snow here?  I wouldn't say, but these are waiting just in case."""
    )
    model_def.define_foamer_facts("""LNER / BR Independent Snowploughs""")

    result.append(model_def)

    return result
