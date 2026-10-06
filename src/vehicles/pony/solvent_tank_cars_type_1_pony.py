from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="TankCarSolventType1",
        base_numeric_id=64770,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarSolventType1",
        base_numeric_id=64780,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarSolventType1",
        base_numeric_id=64790,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_32px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarSolventType1",
        base_numeric_id=64760,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_greebled_alt_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarSolventType1",
        base_numeric_id=64750,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarSolventType1",
        base_numeric_id=64740,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_greebled_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarSolventType1",
        base_numeric_id=64710,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_greebled_alt_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarSolventType1",
        base_numeric_id=64720,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarSolventType1",
        base_numeric_id=64730,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_greebled_alt_32px"
    )

    result.append(model_def)

    return result
