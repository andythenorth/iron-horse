from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="CoveredHopperCarSwingRoofType2",
        base_numeric_id=29480,
        gen=4,
        subtype="A",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_hopper_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CoveredHopperCarSwingRoofType2",
        base_numeric_id=31050,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_hopper_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CoveredHopperCarSwingRoofType2",
        base_numeric_id=28960,
        gen=4,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_hopper_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CoveredHopperCarSwingRoofType2",
        base_numeric_id=26230,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_1cc_filled_hopper_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CoveredHopperCarSwingRoofType2",
        base_numeric_id=26240,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_1cc_filled_hopper_32px"
    )

    result.append(model_def)

    return result
