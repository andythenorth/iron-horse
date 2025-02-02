from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="BolsterCarConsist",
        base_numeric_id=34990,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BolsterCarConsist",
        base_numeric_id=30900,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BolsterCarConsist",
        base_numeric_id=34540,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="4_axle_ng_24px")

    result.append(consist_factory)

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="BolsterCarConsist",
        base_numeric_id=34320,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(consist_factory)

    # no gen 2A, gen 1A continues in pony

    consist_factory = ConsistFactory(
        class_name="BolsterCarConsist",
        base_numeric_id=34330,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="3_axle_gapped_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BolsterCarConsist",
        base_numeric_id=34340,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BolsterCarConsist",
        base_numeric_id=34350,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="4_axle_gapped_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BolsterCarConsist",
        base_numeric_id=34360,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="4_axle_gapped_32px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BolsterCarConsist",
        base_numeric_id=34370,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BolsterCarConsist",
        base_numeric_id=34380,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="4_axle_filled_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BolsterCarConsist",
        base_numeric_id=34390,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="4_axle_gapped_32px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BolsterCarConsist",
        base_numeric_id=34400,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_filled_greebled_24px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BolsterCarConsist",
        base_numeric_id=34290,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_filled_greebled_32px"
    )

    result.append(consist_factory)

    return result
