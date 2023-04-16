from train import (
    PassengerRailbusTrailerCarConsist,
    PaxRailcarTrailerCar,
)


def main():
    # --------------- pony NG----------------------------------------------------------------------

    consist = PassengerRailbusTrailerCarConsist(
        roster_id="pony",
        base_numeric_id=10030,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        cab_id="mumble",
        sprites_complete=True,
    )

    consist.add_unit(
        type=PaxRailcarTrailerCar, chassis="4_axle_ng_24px", tail_light="railcar_24px_1"
    )

    consist = PassengerRailbusTrailerCarConsist(
        roster_id="pony",
        base_numeric_id=13510,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        cab_id="snapper",
        sprites_complete=True,
    )

    consist.add_unit(
        type=PaxRailcarTrailerCar, chassis="4_axle_ng_24px", tail_light="railcar_24px_1"
    )
