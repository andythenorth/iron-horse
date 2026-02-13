from train.model_def import ModelDef


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

    model_def =ModelDef(
        schema_name="AutomobileDoubleDeckEnclosedCar",
        base_numeric_id=4960,
        gen=5,
        subtype="D",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit",
        chassis="2_axle_1cc_filled_20px",
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit",
        chassis="2_axle_1cc_filled_20px",
        rel_spriterow_index=1,
    )

    result.append(model_def)

    return result
