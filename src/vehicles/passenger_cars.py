from train import PassengerCarConsist, PaxCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------
    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=770,
        gen=1,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_16px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=1530,
        gen=1,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_24px")

    # no gen 2 for NG, straight to gen 3

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=800,
        gen=3,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_16px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=600,
        gen=3,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_24px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=860,
        gen=4,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_16px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=660,
        gen=4,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_24px")

    # --------------- pony ----------------------------------------------------------------------
    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=5580,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="2_axle_solid_express_16px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=5590,
        gen=1,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_24px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=2250,
        gen=1,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="6_axle_solid_express_32px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=5600,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="2_axle_solid_express_16px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=5610,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_24px")
    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=2260,
        gen=2,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="6_axle_solid_express_32px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=5620,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="3_axle_solid_express_16px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=5630,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_24px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=2270,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_32px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=5640,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_24px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=3120,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_32px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=740,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_24px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=3130,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_32px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=3300,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_24px")

    consist = PassengerCarConsist(
        roster_id="pony",
        base_numeric_id=1860,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_32px")
