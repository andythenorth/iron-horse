from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="PanoramicCarConsist",
        base_numeric_id=35130,
        gen=4,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="PaxCar", suppress_roof_sprite=True, chassis="4_axle_ng_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="PanoramicCarConsist",
        base_numeric_id=35140,
        gen=4,
        subtype="C",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="PaxCar", suppress_roof_sprite=True, chassis="4_axle_ng_32px"
    )

    result.append(model_def)

    return result
