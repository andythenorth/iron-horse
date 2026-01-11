from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # gen 4 start

    model_def = ModelDef(
        schema_name="CoilCarTarpaulin",
        base_numeric_id=16960,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CoilCarTarpaulin",
        base_numeric_id=17000,
        gen=4,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CoilCarTarpaulin",
        base_numeric_id=26300,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_1cc_filled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CoilCarTarpaulin",
        base_numeric_id=26400,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_1cc_filled_32px"
    )

    result.append(model_def)

    return result
