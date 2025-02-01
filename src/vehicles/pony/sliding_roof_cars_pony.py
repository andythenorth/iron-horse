from train import SlidingRoofCarConsist, FreightCar


def main(roster_id, **kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # gen 5 start, only B and C lengths

    consist_factory = SlidingRoofCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24270,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="2_axle_1cc_filled_24px")

    result.append(consist_factory)

    consist_factory = SlidingRoofCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24280,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")

    result.append(consist_factory)

    consist_factory = SlidingRoofCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=1000,
        gen=5,
        subtype="D",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        type=FreightCar,
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        spriterow_num=0,
    )

    consist_factory.add_unit(
        type=FreightCar,
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        force_spriterow_group_in_output_spritesheet=1, # special case
    )

    result.append(consist_factory)

    return result
