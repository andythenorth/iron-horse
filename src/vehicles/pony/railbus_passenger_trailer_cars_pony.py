from train.train import ModelDef


def main(**kwargs):
    result = []

    # --------------- pony NG----------------------------------------------------------------------

    model_def = ModelDef(
        class_name="PassengerRailbusTrailerCarConsist",
        base_numeric_id=28150,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        cab_id="mumble",
        pax_car_capacity_type="high_capacity",  # specific capacity modifier
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="PaxRailcarTrailerCar",
        chassis="4_axle_ng_24px",
        tail_light="railcar_24px_1",
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerRailbusTrailerCarConsist",
        base_numeric_id=26190,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        cab_id="snapper",
        pax_car_capacity_type="high_capacity",  # specific capacity modifier
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="PaxRailcarTrailerCar",
        chassis="4_axle_ng_24px",
        tail_light="railcar_24px_1",
    )

    result.append(model_def)

    return result
