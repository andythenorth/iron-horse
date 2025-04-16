from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="PanoramicCar",
        base_numeric_id=25940,
        gen=4,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="PaxCarUnit", suppress_roof_sprite=True, chassis="4_axle_ng_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="PanoramicCar",
        base_numeric_id=25960,
        gen=4,
        subtype="C",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="PaxCarUnit", suppress_roof_sprite=True, chassis="4_axle_ng_32px"
    )

    result.append(model_def)

    return result
