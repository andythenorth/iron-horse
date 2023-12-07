from train import PassengerRestaurantCarConsist, PaxRestaurantCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = PassengerRestaurantCarConsist(
        roster_id="pony",
        base_numeric_id=14560,
        gen=1,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxRestaurantCar, chassis="6_axle_solid_express_32px")

    consist = PassengerRestaurantCarConsist(
        roster_id="pony",
        base_numeric_id=14570,
        gen=2,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxRestaurantCar, chassis="6_axle_solid_express_32px")

    consist = PassengerRestaurantCarConsist(
        roster_id="pony",
        base_numeric_id=14580,
        gen=3,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxRestaurantCar, chassis="6_axle_solid_express_32px")

    consist = PassengerRestaurantCarConsist(
        roster_id="pony",
        base_numeric_id=14590,
        gen=4,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxRestaurantCar, chassis="4_axle_solid_express_32px")

    consist = PassengerRestaurantCarConsist(
        roster_id="pony",
        base_numeric_id=14600,
        gen=5,
        subtype="U",
        lgv_capable=True,  # for lolz
        sprites_complete=True,
    )

    consist.add_unit(type=PaxRestaurantCar, chassis="4_axle_solid_express_32px")

    # gen 6 broadly same as gen 5, but new liveries (any other difference?)

    consist = PassengerRestaurantCarConsist(
        roster_id="pony",
        base_numeric_id=14610,
        gen=6,
        subtype="U",
        lgv_capable=True,  # for lolz
        sprites_complete=True,
    )

    consist.add_unit(type=PaxRestaurantCar, chassis="4_axle_solid_express_32px")
