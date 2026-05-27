from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="IntermodalCargoSprinterMiddleCar",
        model_id="brash_middle_unpowered",
        cab_id="brash_cab",
        base_numeric_id=28230,
        gen=5,
        subtype="U",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="IntermodalCarUnit", chassis="4_axle_solid_express_32px"
    )

    result.append(model_def)

    return result
