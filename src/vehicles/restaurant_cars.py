from train import PassengerRestaurantCarConsist, PaxRestaurantCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = PassengerRestaurantCarConsist(
        roster_id="pony",
        base_numeric_id=5520,
        gen=1,
        subtype="U",
        sprites_complete=False,
    )

    consist.add_unit(type=PaxRestaurantCar, chassis="6_axle_solid_express_32px")

    consist = PassengerRestaurantCarConsist(
        roster_id="pony",
        base_numeric_id=5530,
        gen=2,
        subtype="U",
        sprites_complete=False,
    )

    consist.add_unit(type=PaxRestaurantCar, chassis="6_axle_solid_express_32px")

    consist = PassengerRestaurantCarConsist(
        roster_id="pony",
        base_numeric_id=5540,
        gen=3,
        subtype="U",
        sprites_complete=False,
    )

    consist.add_unit(type=PaxRestaurantCar, chassis="6_axle_solid_express_32px")

    consist = PassengerRestaurantCarConsist(
        roster_id="pony",
        base_numeric_id=5550,
        gen=4,
        subtype="U",
        sprites_complete=False,
    )

    consist.add_unit(type=PaxRestaurantCar, chassis="4_axle_solid_express_32px")

    consist = PassengerRestaurantCarConsist(
        roster_id="pony",
        base_numeric_id=5560,
        gen=5,
        subtype="U",
        sprites_complete=False,
    )

    consist.add_unit(type=PaxRestaurantCar, chassis="4_axle_solid_express_32px")

    # gen 6 broadly same as gen 5, but new liveries (any other difference?)

    consist = PassengerRestaurantCarConsist(
        roster_id="pony",
        base_numeric_id=5570,
        gen=6,
        subtype="U",
        sprites_complete=False,
    )

    consist.add_unit(type=PaxRestaurantCar, chassis="4_axle_solid_express_32px")
