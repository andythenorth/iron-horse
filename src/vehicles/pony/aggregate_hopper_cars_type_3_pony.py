from train import HopperCarAggregateConsistType3, FreightCar


def main(roster_id, **kwargs):
    # --------------- narrow gauge -----------------------------------------------------------------
    """
    consist = HopperCarAggregateConsistType3(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=34300,
        gen=3,
        intro_year_offset=20,  # let's be a little bit later for this one
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = HopperCarAggregateConsistType3(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=32850,
        gen=3,
        intro_year_offset=20,  # let's be a little bit later for this one
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_24px")
    """
    # --------------- standard gauge ---------------------------------------------------------------

    consist = HopperCarAggregateConsistType3(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=20280,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = HopperCarAggregateConsistType3(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=22980,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_24px")

    consist = HopperCarAggregateConsistType3(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=20300,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_32px")
