from train.producer import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    """

    model_def =ModelDef(
        schema_name="FoodProductsHopperCarType3",
        base_numeric_id=23480,
        gen=2,
        subtype="A",
        sprites_complete=False,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)


    model_def =ModelDef(
        schema_name="FoodProductsHopperCarType3",
        base_numeric_id=23770,
        gen=2,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_24px")

    result.append(model_def)


    model_def =ModelDef(
        schema_name="FoodProductsHopperCarType3",
        base_numeric_id=24000,
        gen=3,
        subtype="A",
        sprites_complete=False,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)


    model_def =ModelDef(
        schema_name="FoodProductsHopperCarType3",
        base_numeric_id=23430,
        gen=3,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_24px")

    result.append(model_def)
    """

    model_def = ModelDef(
        schema_name="FoodProductsHopperCarType3",
        base_numeric_id=25260,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodProductsHopperCarType3",
        base_numeric_id=25240,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodProductsHopperCarType3",
        base_numeric_id=25270,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_chute_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodProductsHopperCarType3",
        base_numeric_id=25250,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_chute_greebled_alt_32px"
    )

    result.append(model_def)

    return result
