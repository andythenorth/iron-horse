from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="BulkOpenCarAggregateConsistType1",
        base_numeric_id=32970,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_sparse_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BulkOpenCarAggregateConsistType1",
        base_numeric_id=32990,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_sparse_32px")

    result.append(consist_factory)

    return result
