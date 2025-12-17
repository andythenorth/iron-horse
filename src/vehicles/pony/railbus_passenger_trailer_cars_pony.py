from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- pony NG----------------------------------------------------------------------

    model_def = ModelDef(
        schema_name="PassengerRailbusTrailerCar",
        base_numeric_id=20260,
        gen=3,
        subtype="U",
        base_track_type="NG",
        cab_id="mumble",
        pax_car_capacity_type="high_capacity",  # specific capacity modifier
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="PaxRailcarTrailerCarUnit",
        chassis="4_axle_ng_24px",
        tail_light="railcar_24px_1",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="PassengerRailbusTrailerCar",
        base_numeric_id=20270,
        gen=4,
        subtype="U",
        base_track_type="NG",
        cab_id="snapper",
        pax_car_capacity_type="high_capacity",  # specific capacity modifier
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="PaxRailcarTrailerCarUnit",
        chassis="4_axle_ng_24px",
        tail_light="railcar_24px_1",
    )

    result.append(model_def)

    return result
