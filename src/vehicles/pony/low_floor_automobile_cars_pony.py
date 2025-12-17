from train.producer import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # intro gen 4

    model_def = ModelDef(
        schema_name="AutomobileLowFloorCar",
        base_numeric_id=26720,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit", chassis="jacobs_solid_express_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="AutomobileLowFloorCar",
        base_numeric_id=33040,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit",
        chassis="jacobs_solid_express_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="AutomobileLowFloorCar",
        base_numeric_id=26740,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit", chassis="jacobs_solid_express_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="AutomobileLowFloorCar",
        base_numeric_id=35070,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit",
        chassis="jacobs_solid_express_32px",
    )

    result.append(model_def)

    return result
