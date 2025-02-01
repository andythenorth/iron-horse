from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------
    """
    consist_factory = ConsistFactory(
        class_name="HopperCarAggregateConsistType3",
        base_numeric_id=34300,
        gen=3,
        intro_year_offset=20,  # let's be a little bit later for this one
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=False,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarAggregateConsistType3",
        base_numeric_id=32850,
        gen=3,
        intro_year_offset=20,  # let's be a little bit later for this one
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=False,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_ng_24px")

    result.append(consist_factory)
   """
    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="HopperCarAggregateConsistType3",
        base_numeric_id=20280,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_gapped_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarAggregateConsistType3",
        base_numeric_id=22980,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_filled_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarAggregateConsistType3",
        base_numeric_id=20300,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_filled_32px")

    result.append(consist_factory)

    return result
