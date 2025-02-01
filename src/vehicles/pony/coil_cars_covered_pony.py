from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # start gen 4

    consist_factory = ConsistFactory(
        class_name="CoilCarCoveredConsist",
        base_numeric_id=30190,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="CoilCarCoveredConsist",
        base_numeric_id=30200,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_gapped_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="CoilCarCoveredConsist",
        base_numeric_id=30210,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_gapped_32px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="CoilCarCoveredConsist",
        base_numeric_id=30220,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_1cc_filled_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="CoilCarCoveredConsist",
        base_numeric_id=30230,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_1cc_filled_32px")

    result.append(consist_factory)

    return result
