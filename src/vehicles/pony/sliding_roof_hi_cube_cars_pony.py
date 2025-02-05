from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="SlidingRoofCarConsistHiCube",
        base_numeric_id=30730,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_filled_24px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="SlidingRoofCarConsistHiCube",
        base_numeric_id=18520,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_filled_32px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="SlidingRoofCarConsistHiCube",
        base_numeric_id=840,
        gen=5,
        subtype="D",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar",
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        spriterow_num=0,
    )

    model_type_factory.define_unit(
        class_name="FreightCar",
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        force_spriterow_group_in_output_spritesheet=1,  # special case
    )

    result.append(model_type_factory)

    return result
