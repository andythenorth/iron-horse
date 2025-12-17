from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        schema_name="PanoramicCar",
        base_numeric_id=25940,
        gen=4,
        subtype="B",
        livery_group_name="gen_4_ng_pax_liveries",  # override default liveries from gestalt
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="PaxCarUnit", suppress_roof_sprite=True, chassis="4_axle_ng_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="PanoramicCar",
        base_numeric_id=25960,
        gen=4,
        subtype="C",
        livery_group_name="gen_4_ng_pax_liveries",  # override default liveries from gestalt
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="PaxCarUnit", suppress_roof_sprite=True, chassis="4_axle_ng_32px"
    )

    result.append(model_def)

    return result
