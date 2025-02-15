from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="FarmProductsHopperCarType1",
        base_numeric_id=31350,
        gen=2,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    # no gen 2 for NG, straight to gen 3

    model_def = ModelDef(
        class_name="FarmProductsHopperCarType1",
        base_numeric_id=31360,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_ng_sparse_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmProductsHopperCarType1",
        base_numeric_id=31370,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_ng_sparse_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="FarmProductsHopperCarType1",
        base_numeric_id=23480,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmProductsHopperCarType1",
        base_numeric_id=23770,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="2_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmProductsHopperCarType1",
        base_numeric_id=24000,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmProductsHopperCarType1",
        base_numeric_id=23430,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="2_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmProductsHopperCarType1",
        base_numeric_id=23440,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmProductsHopperCarType1",
        base_numeric_id=23450,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="2_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmProductsHopperCarType1",
        base_numeric_id=23460,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="2_axle_chute_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmProductsHopperCarType1",
        base_numeric_id=23470,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="4_axle_chute_greebled_alt_32px"
    )

    result.append(model_def)

    return result
