from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="MineralCoveredHopperCarLimeConsistType1",
        base_numeric_id=25990,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="2_axle_gapped_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="MineralCoveredHopperCarLimeConsistType1",
        base_numeric_id=26000,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="2_axle_gapped_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="MineralCoveredHopperCarLimeConsistType1",
        base_numeric_id=26010,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="2_axle_gapped_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="MineralCoveredHopperCarLimeConsistType1",
        base_numeric_id=26020,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="2_axle_gapped_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="MineralCoveredHopperCarLimeConsistType1",
        base_numeric_id=26070,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_16px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="MineralCoveredHopperCarLimeConsistType1",
        base_numeric_id=26030,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_24px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="MineralCoveredHopperCarLimeConsistType1",
        base_numeric_id=26040,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_half_filled_greebled_32px"
    )

    result.append(consist_factory)

    return result
