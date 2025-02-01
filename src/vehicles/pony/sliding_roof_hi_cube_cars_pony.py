from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="SlidingRoofCarConsistHiCube",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30730,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_filled_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="SlidingRoofCarConsistHiCube",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=18520,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_filled_32px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="SlidingRoofCarConsistHiCube",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=840,
        gen=5,
        subtype="D",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar",
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        spriterow_num=0,
    )

    consist_factory.add_unit(
        class_name="FreightCar",
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        force_spriterow_group_in_output_spritesheet=1,  # special case
    )

    result.append(consist_factory)

    return result
