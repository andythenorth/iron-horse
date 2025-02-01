from train import AutomobileCarConsist, AutomobileCarSymmetric


def main(roster_id, **kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    # no gen 1, straight to gen 2

    # !! 16px version needs spritelayer cargo support finishing for 16px cargo sprites
    """
    consist_factory = AutomobileCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=22570,
        gen=2,
        subtype="A",
        sprites_complete=False,
    )

    consist_factory.add_unit(class_name=AutomobileCarSymmetric, chassis="2_axle_solid_express_16px")
    """
    consist_factory = AutomobileCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=22540,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name=AutomobileCarSymmetric, chassis="3_axle_solid_express_24px"
    )

    result.append(consist_factory)

    consist_factory = AutomobileCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24800,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name=AutomobileCarSymmetric, chassis="4_axle_solid_express_32px"
    )

    result.append(consist_factory)

    consist_factory = AutomobileCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=22550,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name=AutomobileCarSymmetric, chassis="2_axle_filled_24px")

    result.append(consist_factory)

    consist_factory = AutomobileCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24770,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name=AutomobileCarSymmetric, chassis="4_axle_solid_express_32px"
    )

    result.append(consist_factory)

    consist_factory = AutomobileCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=22560,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name=AutomobileCarSymmetric, chassis="2_axle_filled_greebled_24px"
    )

    result.append(consist_factory)

    consist_factory = AutomobileCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24760,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name=AutomobileCarSymmetric, chassis="4_axle_filled_greebled_32px"
    )

    result.append(consist_factory)

    return result
