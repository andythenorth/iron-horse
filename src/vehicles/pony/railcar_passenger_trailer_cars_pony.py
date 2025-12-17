from train.producer import ModelDef


def main(**kwargs):
    result = []

    # --------------- pony NG----------------------------------------------------------------------

    # Pony NG uses railbus trailers, not railcar

    # --------------- standard gauge ---------------------------------------------------------------
    # gen 3 could be added but needs the engine grilles replacing with pax car pixels

    model_def = ModelDef(
        schema_name="PassengerRailcarTrailerCar",
        base_numeric_id=17130,
        gen=4,
        subtype="U",
        sprites_complete=True,
        cab_id="slammer",
    )

    model_def.add_unit_def(
        unit_cls_name="PaxRailcarTrailerCarUnit",
        chassis="4_axle_solid_pax_mail_32px",
        tail_light="railcar_32px_2",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="PassengerRailcarTrailerCar",
        base_numeric_id=26060,
        gen=4,
        subtype="U",
        sprites_complete=True,
        cab_id="geronimo",
    )

    model_def.add_unit_def(
        unit_cls_name="PaxRailcarTrailerCarUnit",
        chassis="4_axle_solid_pax_mail_32px",
        tail_light="railcar_32px_2",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="PassengerRailcarTrailerCar",
        base_numeric_id=27170,
        gen=5,
        subtype="U",
        sprites_complete=True,
        cab_id="tin_rocket",
    )

    model_def.add_unit_def(
        unit_cls_name="PaxRailcarTrailerCarUnit",
        chassis="4_axle_solid_pax_mail_32px",
        tail_light="railcar_32px_3",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="PassengerRailcarTrailerCar",
        base_numeric_id=25140,
        gen=5,
        subtype="U",
        sprites_complete=True,
        cab_id="breeze",
    )

    model_def.add_unit_def(
        unit_cls_name="PaxRailcarTrailerCarUnit",
        chassis="4_axle_solid_pax_mail_32px",
        tail_light="railcar_32px_3",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="PassengerRailcarTrailerCar",
        base_numeric_id=25580,
        gen=6,
        subtype="U",
        cab_id="happy_train",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="PaxRailcarTrailerCarUnit",
        chassis="4_axle_solid_pax_mail_32px",
        tail_light="railcar_32px_2",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="PassengerRailcarTrailerCar",
        base_numeric_id=25400,
        gen=6,
        subtype="U",
        cab_id="zeus",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="PaxRailcarTrailerCarUnit",
        chassis="4_axle_solid_pax_mail_32px",
        tail_light="railcar_32px_2",
    )

    result.append(model_def)

    return result
