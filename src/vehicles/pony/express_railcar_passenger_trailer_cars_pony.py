from train.producer import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="PassengerExpressRailcarTrailerCar",
        base_numeric_id=15350,
        gen=3,
        subtype="U",
        cab_id="kraken",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="PaxRailcarTrailerCarUnit",
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
        suppress_roof_sprite=True,
        repeat=2,
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="PassengerExpressRailcarTrailerCar",
        base_numeric_id=1940,
        gen=3,
        subtype="U",
        cab_id="high_flyer",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="PaxRailcarTrailerCarUnit",
        chassis="4_axle_solid_pax_mail_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="PassengerExpressRailcarTrailerCar",
        base_numeric_id=15340,
        gen=4,
        subtype="U",
        cab_id="turbulent",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="PaxRailcarTrailerCarUnit",
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="PassengerExpressRailcarTrailerCar",
        base_numeric_id=2170,
        gen=4,
        subtype="U",
        cab_id="sunshine_coast",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="PaxRailcarTrailerCarUnit",
        chassis="4_axle_solid_pax_mail_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="PassengerExpressRailcarTrailerCar",
        base_numeric_id=1010,
        gen=5,
        subtype="U",
        cab_id="typhoon",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="PaxRailcarTrailerCarUnit",
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="PassengerExpressRailcarTrailerCar",
        base_numeric_id=30,
        gen=5,
        subtype="U",
        cab_id="olympic",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="PaxRailcarTrailerCarUnit",
        chassis="4_axle_solid_pax_mail_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="PassengerExpressRailcarTrailerCar",
        base_numeric_id=6380,
        gen=6,
        subtype="U",
        cab_id="nimbus",
        lgv_capable=True,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="PaxRailcarTrailerCarUnit",
        chassis="high_speed_32px",
        tail_light="railcar_32px_5",
        suppress_roof_sprite=True,
        repeat=2,
    )

    result.append(model_def)

    return result
