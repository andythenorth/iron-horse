from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType1",
        base_numeric_id=28790,
        gen=2,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FlatCarDropCentreAsymmetricUnit",
        chassis="2_axle_running_gear_only_alt_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType1",
        base_numeric_id=28800,
        gen=2,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FlatCarDropCentreAsymmetricUnit",
        chassis="4_axle_running_gear_only_alt_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType1",
        base_numeric_id=28810,
        gen=3,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FlatCarDropCentreAsymmetricUnit",
        chassis="2_axle_running_gear_only_alt_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType1",
        base_numeric_id=28820,
        gen=3,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FlatCarDropCentreAsymmetricUnit",
        chassis="4_axle_running_gear_only_alt_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType1",
        base_numeric_id=32400,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FlatCarDropCentreAsymmetricUnit",
        chassis="2_axle_running_gear_only_alt_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType1",
        base_numeric_id=32410,
        gen=4,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FlatCarDropCentreAsymmetricUnit",
        chassis="4_axle_running_gear_only_alt_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType1",
        base_numeric_id=32420,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FlatCarDropCentreAsymmetricUnit",
        chassis="2_axle_running_gear_only_alt_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType1",
        base_numeric_id=32430,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FlatCarDropCentreAsymmetricUnit",
        chassis="4_axle_running_gear_only_alt_32px",
    )

    result.append(model_def)

    return result
