from train import FoodHopperCarConsistType1, FreightCar


def main(roster_id, **kwargs):
    """
    # --------------- narrow gauge -----------------------------------------------------------------
    consist = FoodHopperCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=31350,
        gen=2,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # no gen 2 for NG, straight to gen 3

    consist = FoodHopperCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=31360,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = FoodHopperCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=31370,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_24px")

    # --------------- standard gauge ---------------------------------------------------------------

    consist = FoodHopperCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23480,
        gen=2,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = FoodHopperCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23770,
        gen=2,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = FoodHopperCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24000,
        gen=3,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = FoodHopperCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23430,
        gen=3,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")
    """
    consist = FoodHopperCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=31150,
        gen=4,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = FoodHopperCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=32300,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = FoodHopperCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35330,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")

    consist = FoodHopperCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35340,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_chute_greebled_alt_32px")
