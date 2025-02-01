from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="IntermodalLowFloorCarConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24450,
        gen=5,
        subtype="A",
        sprites_complete=True,
        consist_ruleset="1_unit_sets",  # special case for single unit low-floor intermodals (they're PFAs eh)
    )

    consist_factory.add_unit(
        class_name="IntermodalCar", chassis="2_axle_1cc_low_floor_16px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="IntermodalLowFloorCarConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24460,
        gen=5,
        subtype="B",
        sprites_complete=True,
        consist_ruleset="2_unit_sets",  # special case for 2 unit low-floor intermodals (they're FLAs eh)
    )
    consist_factory.add_unit(
        class_name="IntermodalCar", chassis="4_axle_1cc_low_floor_24px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="IntermodalLowFloorCarConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24470,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="IntermodalCar", chassis="4_axle_1cc_low_floor_32px"
    )

    result.append(consist_factory)

    return result
