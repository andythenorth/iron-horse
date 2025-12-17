from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        schema_name="LogCar",
        base_numeric_id=27810,
        gen=1,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_ng_spine_16px")

    result.append(model_def)

    # no gen 2 for NG, straight to gen 3

    model_def = ModelDef(
        schema_name="LogCar",
        base_numeric_id=28690,
        gen=3,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_ng_spine_16px")

    result.append(model_def)

    """ # restore in next version

    model_def =ModelDef(
        schema_name="LogCar",
        base_numeric_id=36240,
        gen=4,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_ng_spine_16px")

    result.append(model_def)
    """
    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="LogCar",
        base_numeric_id=30030,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="LogCar",
        base_numeric_id=31770,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="LogCar",
        base_numeric_id=30070,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_filled_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="LogCar",
        base_numeric_id=30050,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="LogCar",
        base_numeric_id=29990,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_filled_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="LogCar",
        base_numeric_id=28670,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_32px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="LogCar",
        base_numeric_id=30010,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_filled_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="LogCar",
        base_numeric_id=17010,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_1cc_filled_32px"
    )

    result.append(model_def)

    return result
