from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="PipeCarConsist",
        base_numeric_id=20010,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="4_axle_filled_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="PipeCarConsist",
        base_numeric_id=28490,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="4_axle_gapped_32px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="PipeCarConsist",
        base_numeric_id=35590,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_1cc_filled_24px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="PipeCarConsist",
        base_numeric_id=34830,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_1cc_filled_32px"
    )

    result.append(consist_factory)

    return result
