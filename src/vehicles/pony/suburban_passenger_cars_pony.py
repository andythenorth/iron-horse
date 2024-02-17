from train import PassengerSuburbanCarConsist, PaxCar


def main(roster_id):
    # --------------- pony NG----------------------------------------------------------------------

    # no NG suburban cars in pony

    # --------------- standard gauge ---------------------------------------------------------------
    # no gen 1, the capacity difference is negligible compared to standard pax

    consist = PassengerSuburbanCarConsist(
        roster_id=roster_id,
        base_numeric_id=12350,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="3_axle_solid_express_16px")

    consist = PassengerSuburbanCarConsist(
        roster_id=roster_id,
        base_numeric_id=9790,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_24px")

    consist = PassengerSuburbanCarConsist(
        roster_id=roster_id,
        base_numeric_id=12330,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="3_axle_solid_express_16px")

    consist = PassengerSuburbanCarConsist(
        roster_id=roster_id,
        base_numeric_id=9800,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_24px")

    consist = PassengerSuburbanCarConsist(
        roster_id=roster_id,
        base_numeric_id=13610,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="6_axle_solid_express_32px")

    consist = PassengerSuburbanCarConsist(
        roster_id=roster_id,
        base_numeric_id=12150,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_24px")

    consist = PassengerSuburbanCarConsist(
        roster_id=roster_id,
        base_numeric_id=12300,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_32px")

    consist = PassengerSuburbanCarConsist(
        roster_id=roster_id,
        base_numeric_id=12140,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_24px")

    consist = PassengerSuburbanCarConsist(
        roster_id=roster_id,
        base_numeric_id=12320,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_32px")

    # gen 6 broadly same as gen 5, but new liveries (any other difference?)

    consist = PassengerSuburbanCarConsist(
        roster_id=roster_id,
        base_numeric_id=10620,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_24px")

    consist = PassengerSuburbanCarConsist(
        roster_id=roster_id,
        base_numeric_id=12310,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_32px")
