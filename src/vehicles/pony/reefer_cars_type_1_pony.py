from train import ReeferCarConsistType1, ExpressCar


def main(roster_id, **kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------    # no gen 1 reefer - straight to gen 2

    consist_factory = ReeferCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24180,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="ExpressCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_16px",
    )

    result.append(consist_factory)

    consist_factory = ReeferCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24190,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="ExpressCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_16px",
    )

    result.append(consist_factory)

    consist_factory = ReeferCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=16430,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="ExpressCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="3_axle_solid_express_24px",
    )

    result.append(consist_factory)

    consist_factory = ReeferCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24200,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="ExpressCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_16px",
    )

    result.append(consist_factory)

    consist_factory = ReeferCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24210,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="ExpressCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_24px",
    )

    result.append(consist_factory)

    consist_factory = ReeferCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24220,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="ExpressCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_filled_32px",
    )

    result.append(consist_factory)

    consist_factory = ReeferCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24230,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="ExpressCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_greebled_24px",
    )

    result.append(consist_factory)

    consist_factory = ReeferCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24240,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="ExpressCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_filled_greebled_32px",
    )

    result.append(consist_factory)

    return result
