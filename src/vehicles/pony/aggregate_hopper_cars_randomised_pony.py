from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        schema_name="HopperCarAggregateRandomised",
        base_numeric_id=28910,
        gen=1,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarAggregateRandomised",
        base_numeric_id=28930,
        gen=3,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarAggregateRandomised",
        base_numeric_id=28750,
        gen=3,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="HopperCarAggregateRandomised",
        base_numeric_id=28770,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarAggregateRandomised",
        base_numeric_id=28790,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarAggregateRandomised",
        base_numeric_id=28810,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarAggregateRandomised",
        base_numeric_id=28830,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarAggregateRandomised",
        base_numeric_id=28850,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarAggregateRandomised",
        base_numeric_id=28870,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit",
        chassis="empty_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarAggregateRandomised",
        base_numeric_id=28890,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarAggregateRandomised",
        base_numeric_id=20350,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarAggregateRandomised",
        base_numeric_id=21970,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_32px")

    result.append(model_def)

    return result
