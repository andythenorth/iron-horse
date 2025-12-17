from train.producer import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------    # intro gen 4

    model_def = ModelDef(
        schema_name="AutomobileDoubleDeckEnclosedCar",
        base_numeric_id=34560,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit", chassis="jacobs_solid_express_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="AutomobileDoubleDeckEnclosedCar",
        base_numeric_id=34580,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit", chassis="jacobs_solid_express_32px"
    )

    result.append(model_def)

    return result
