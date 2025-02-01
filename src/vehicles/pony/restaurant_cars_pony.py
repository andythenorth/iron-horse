from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="PassengerRestaurantCarConsist",
        base_numeric_id=34560,
        gen=1,
        subtype="U",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="PaxRestaurantCar", chassis="6_axle_solid_express_32px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="PassengerRestaurantCarConsist",
        base_numeric_id=34570,
        gen=2,
        subtype="U",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="PaxRestaurantCar", chassis="6_axle_solid_express_32px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="PassengerRestaurantCarConsist",
        base_numeric_id=34580,
        gen=3,
        subtype="U",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="PaxRestaurantCar", chassis="6_axle_solid_express_32px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="PassengerRestaurantCarConsist",
        base_numeric_id=34590,
        gen=4,
        subtype="U",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="PaxRestaurantCar", chassis="4_axle_solid_express_32px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="PassengerRestaurantCarConsist",
        base_numeric_id=34600,
        gen=5,
        subtype="U",
        lgv_capable=True,  # for lolz
        liveries="gen_5_and_6_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="PaxRestaurantCar", chassis="4_axle_solid_express_32px"
    )

    result.append(consist_factory)

    return result
