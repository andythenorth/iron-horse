from train import PassengerCarConsist, PaxCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------
    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=1530,
        gen=1,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_24px")

    # no gen 2 for NG, straight to gen 3

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=600,
        gen=3,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_24px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=660,
        gen=4,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_24px")

    # --------------- pony ----------------------------------------------------------------------
    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=2250,
        gen=1,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="6_axle_solid_express_32px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=2260,
        gen=2,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="6_axle_solid_express_32px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=2270,
        gen=3,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="6_axle_solid_express_32px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=3120,
        gen=4,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_32px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=3130,
        gen=5,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_32px")

    # gen 6 broadly same as gen 5, but new liveries (any other difference?)

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=1860,
        gen=6,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_32px")
