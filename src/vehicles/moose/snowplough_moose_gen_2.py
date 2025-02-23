from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SnowploughEngine",
        model_type_id="snowplough_moose_gen_2",
        base_numeric_id=34890,
        name="Snowplough",
        gen=2,
        speed=75,
        liveries=["VANILLA"],
        cabbage_new_livery_system=True,
        sprites_complete=False,
    )

    model_def.add_unit_def(class_name="SnowploughUnit", weight=50, vehicle_length=4)

    model_def.define_description("""MOOSE.""")
    model_def.define_foamer_facts("""MOOSE""")

    result.append(model_def)

    return result
