from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="MineralCoveredHopperCarLimeConsistType3",
        base_numeric_id=34840,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="2_axle_gapped_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="MineralCoveredHopperCarLimeConsistType3",
        base_numeric_id=33820,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="2_axle_gapped_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="MineralCoveredHopperCarLimeConsistType3",
        base_numeric_id=33030,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_chute_greebled_16px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="MineralCoveredHopperCarLimeConsistType3",
        base_numeric_id=34850,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_chute_greebled_24px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="MineralCoveredHopperCarLimeConsistType3",
        base_numeric_id=36340,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_filled_greebled_32px"
    )

    result.append(consist_factory)

    return result
