from train import FoodHopperCarConsistType3, FreightCar


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------
    """
    consist = FoodHopperCarConsistType3(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23480,
        gen=2,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = FoodHopperCarConsistType3(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23770,
        gen=2,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = FoodHopperCarConsistType3(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24000,
        gen=3,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = FoodHopperCarConsistType3(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23430,
        gen=3,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")
    """
    consist = FoodHopperCarConsistType3(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=34200,
        gen=4,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = FoodHopperCarConsistType3(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35070,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = FoodHopperCarConsistType3(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=33040,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = FoodHopperCarConsistType3(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=36970,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")
