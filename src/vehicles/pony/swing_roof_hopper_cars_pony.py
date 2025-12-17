from train.producer import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="CoveredHopperCarSwingRoof",
        base_numeric_id=26200,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_1cc_filled_hoppers_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CoveredHopperCarSwingRoof",
        base_numeric_id=16660,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_1cc_filled_hoppers_32px"
    )

    result.append(model_def)

    return result
