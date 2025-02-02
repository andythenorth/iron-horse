from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # gen 5 start, only B and C lengths

    consist_factory = ConsistFactory(
        class_name="TarpaulinCarConsistType1",
        base_numeric_id=25530,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_filled_greebled_24px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TarpaulinCarConsistType1",
        base_numeric_id=35610,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_filled_greebled_32px"
    )

    result.append(consist_factory)

    return result
