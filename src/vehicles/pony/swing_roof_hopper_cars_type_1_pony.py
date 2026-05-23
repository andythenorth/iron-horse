from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="CoveredHopperCarSwingRoofType1",
        base_numeric_id=29220,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_hopper_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CoveredHopperCarSwingRoofType1",
        base_numeric_id=32300,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_hopper_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CoveredHopperCarSwingRoofType1",
        base_numeric_id=26200,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_1cc_filled_hopper_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CoveredHopperCarSwingRoofType1",
        base_numeric_id=16660,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_1cc_filled_hopper_32px"
    )

    result.append(model_def)

    return result
