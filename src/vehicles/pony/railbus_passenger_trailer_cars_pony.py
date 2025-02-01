from train import (
    PassengerRailbusTrailerCarConsist,
)


def main(roster_id, **kwargs):
    result = []

    # --------------- pony NG----------------------------------------------------------------------

    consist_factory = PassengerRailbusTrailerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=28150,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        cab_id="mumble",
        pax_car_capacity_type="high_capacity",  # specific capacity modifier
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="PaxRailcarTrailerCar",
        chassis="4_axle_ng_24px",
        tail_light="railcar_24px_1",
    )

    result.append(consist_factory)

    consist_factory = PassengerRailbusTrailerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=26190,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        cab_id="snapper",
        pax_car_capacity_type="high_capacity",  # specific capacity modifier
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="PaxRailcarTrailerCar",
        chassis="4_axle_ng_24px",
        tail_light="railcar_24px_1",
    )

    result.append(consist_factory)

    return result
