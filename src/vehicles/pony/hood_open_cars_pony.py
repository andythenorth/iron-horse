from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # only type A for gen 1

    consist_factory = ConsistFactory(
        class_name="OpenCarHoodConsist",
        base_numeric_id=16520,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(consist_factory)

    # no type A for gen 2, gen 1 type A continues, also no gen 2 type B

    consist_factory = ConsistFactory(
        class_name="OpenCarHoodConsist",
        base_numeric_id=16540,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="OpenCarHoodConsist",
        base_numeric_id=16550,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_gapped_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="OpenCarHoodConsist",
        base_numeric_id=16560,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="OpenCarHoodConsist",
        base_numeric_id=16570,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_filled_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="OpenCarHoodConsist",
        base_numeric_id=16580,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar", chassis="2_axle_filled_greebled_24px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="OpenCarHoodConsist",
        base_numeric_id=16590,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_1cc_filled_32px")

    result.append(consist_factory)

    return result
