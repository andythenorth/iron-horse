from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="HopperCarAggregateType3",
        base_numeric_id=31190,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_hopper_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarAggregateType3",
        base_numeric_id=29760,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_hopper_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarAggregateType3",
        base_numeric_id=29260,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_hopper_32px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarAggregateType3",
        base_numeric_id=20280,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_hopper_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarAggregateType3",
        base_numeric_id=22980,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_filled_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarAggregateType3",
        base_numeric_id=20300,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_filled_greebled_alt_32px")

    result.append(model_def)

    return result
