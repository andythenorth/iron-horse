from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="CarbonBlackHopperCarRandomised",
        base_numeric_id=32740,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_hopper_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CarbonBlackHopperCarRandomised",
        base_numeric_id=32750,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_hopper_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CarbonBlackHopperCarRandomised",
        base_numeric_id=32690,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_hopper_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CarbonBlackHopperCarRandomised",
        base_numeric_id=32700,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_hopper_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CarbonBlackHopperCarRandomised",
        base_numeric_id=32710,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_hopper_32px"
    )

    result.append(model_def)

    return result
