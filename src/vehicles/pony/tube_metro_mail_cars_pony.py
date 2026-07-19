from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- Metro ----------------------------------------------------------------------

    model_def = ModelDef(
        schema_name="MailMetroCarTube",
        base_numeric_id=32620,
        gen=1,
        subtype="C",
        base_track_type="METRO",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="MailMetroCarUnit",
        chassis="metro_heavy_32px",
        suppress_roof_sprite=True,
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailMetroCarTube",
        base_numeric_id=32630,
        gen=2,
        subtype="C",
        base_track_type="METRO",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="MailMetroCarUnit",
        chassis="metro_heavy_32px",
        suppress_roof_sprite=True,
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MailMetroCarTube",
        base_numeric_id=32640,
        gen=3,
        subtype="C",
        base_track_type="METRO",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="MailMetroCarUnit",
        chassis="metro_heavy_32px",
        suppress_roof_sprite=True,
    )

    result.append(model_def)

    return result
