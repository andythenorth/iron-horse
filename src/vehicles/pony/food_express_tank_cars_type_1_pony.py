from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    # note that NG uses FreightCarUnit not ExpressCarUnit, as there is no adjustment of capacity for higher speed
    # this is a bit of an inconsistency in the set design, but it's a tradeoff where the alternative is having no NG food tanker at all, or bizarrely low capacity

    model_def = ModelDef(
        schema_name="FoodExpressTankCarType1",
        base_numeric_id=19960,
        gen=2,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressTankCarType1",
        base_numeric_id=19980,
        gen=3,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_ng_sparse_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressTankCarType1",
        base_numeric_id=20000,
        gen=3,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_ng_sparse_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressTankCarType1",
        base_numeric_id=24800,
        gen=4,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_ng_sparse_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressTankCarType1",
        base_numeric_id=24290,
        gen=4,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_ng_sparse_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------
    # no gen 1 for food tank cars - straight to gen 2

    model_def = ModelDef(
        schema_name="FoodExpressTankCarType1",
        base_numeric_id=17200,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="ExpressCarUnit", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressTankCarType1",
        base_numeric_id=17210,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="ExpressCarUnit", chassis="3_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressTankCarType1",
        base_numeric_id=17220,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit", chassis="3_axle_filled_greebled_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressTankCarType1",
        base_numeric_id=17230,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit", chassis="4_axle_sparse_greebled_alt_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressTankCarType1",
        base_numeric_id=28190,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit", chassis="4_axle_sparse_greebled_alt_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressTankCarType1",
        base_numeric_id=28440,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit", chassis="3_axle_filled_greebled_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressTankCarType1",
        base_numeric_id=16970,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit", chassis="4_axle_sparse_greebled_alt_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressTankCarType1",
        base_numeric_id=28180,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit", chassis="4_axle_sparse_greebled_alt_32px"
    )

    result.append(model_def)

    return result
