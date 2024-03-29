from train import PassengerRestaurantCarConsist, PaxRestaurantCar


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------

    consist = PassengerRestaurantCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=34560,
        gen=1,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxRestaurantCar, chassis="6_axle_solid_express_32px")

    consist = PassengerRestaurantCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=34570,
        gen=2,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxRestaurantCar, chassis="6_axle_solid_express_32px")

    consist = PassengerRestaurantCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=34580,
        gen=3,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxRestaurantCar, chassis="6_axle_solid_express_32px")

    consist = PassengerRestaurantCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=34590,
        gen=4,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxRestaurantCar, chassis="4_axle_solid_express_32px")

    consist = PassengerRestaurantCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=34600,
        gen=5,
        subtype="U",
        lgv_capable=True,  # for lolz
        liveries="gen_5_and_6_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    consist.add_unit(type=PaxRestaurantCar, chassis="4_axle_solid_express_32px")
