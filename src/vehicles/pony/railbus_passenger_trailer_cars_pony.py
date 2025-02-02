from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- pony NG----------------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="PassengerRailbusTrailerCarConsist",
        base_numeric_id=28150,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        cab_id="mumble",
        pax_car_capacity_type="high_capacity",  # specific capacity modifier
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="PaxRailcarTrailerCar",
        chassis="4_axle_ng_24px",
        tail_light="railcar_24px_1",
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="PassengerRailbusTrailerCarConsist",
        base_numeric_id=26190,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        cab_id="snapper",
        pax_car_capacity_type="high_capacity",  # specific capacity modifier
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="PaxRailcarTrailerCar",
        chassis="4_axle_ng_24px",
        tail_light="railcar_24px_1",
    )

    result.append(consist_factory)

    return result
