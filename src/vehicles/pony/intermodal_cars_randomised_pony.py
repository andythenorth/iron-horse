from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------


    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="IntermodalCarRandomised",
        base_numeric_id=34600,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="2_axle_1cc_filled_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="IntermodalCarRandomised",
        base_numeric_id=34620,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="4_axle_1cc_filled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="IntermodalCarRandomised",
        base_numeric_id=34640,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="4_axle_1cc_filled_32px"
    )

    result.append(model_def)

    return result
