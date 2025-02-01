from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="IntermodalCarConsist",
        base_numeric_id=28350,
        gen=3,
        intro_year_offset=15,  # let's be a little bit later for this one
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="IntermodalCar", chassis="4_axle_ng_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="IntermodalCarConsist",
        base_numeric_id=28360,
        gen=3,
        intro_year_offset=15,  # let's be a little bit later for this one
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="IntermodalCar", chassis="4_axle_ng_24px")

    result.append(consist_factory)

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="IntermodalCarConsist",
        base_numeric_id=28370,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="IntermodalCar", chassis="2_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="IntermodalCarConsist",
        base_numeric_id=28380,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="IntermodalCar", chassis="4_axle_gapped_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="IntermodalCarConsist",
        base_numeric_id=28390,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="IntermodalCar", chassis="4_axle_gapped_32px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="IntermodalCarConsist",
        base_numeric_id=28400,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="IntermodalCar", chassis="2_axle_1cc_filled_16px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="IntermodalCarConsist",
        base_numeric_id=28410,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="IntermodalCar", chassis="4_axle_1cc_filled_24px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="IntermodalCarConsist",
        base_numeric_id=28420,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="IntermodalCar", chassis="4_axle_1cc_filled_32px"
    )

    result.append(consist_factory)

    return result
