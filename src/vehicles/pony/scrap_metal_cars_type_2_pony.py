from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="BulkOpenCarScrapMetalConsistType2",
        base_numeric_id=32120,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_16px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BulkOpenCarScrapMetalConsistType2",
        base_numeric_id=32140,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_24px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BulkOpenCarScrapMetalConsistType2",
        base_numeric_id=32160,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_gapped_greebled_32px"
    )

    result.append(consist_factory)

    return result
