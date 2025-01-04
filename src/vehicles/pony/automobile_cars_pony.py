from train import AutomobileCarConsist, AutomobileCarSymmetric


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------

    # no gen 1, straight to gen 2

    # !! 16px version needs spritelayer cargo support finishing for 16px cargo sprites
    """
    consist = AutomobileCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=22570,
        gen=2,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=AutomobileCarSymmetric, chassis="2_axle_solid_express_16px")
    """
    consist = AutomobileCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=22540,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCarSymmetric, chassis="3_axle_solid_express_24px")

    consist = AutomobileCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24800,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCarSymmetric, chassis="4_axle_solid_express_32px")

    consist = AutomobileCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=22550,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCarSymmetric, chassis="2_axle_filled_24px")

    consist = AutomobileCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24770,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCarSymmetric, chassis="4_axle_solid_express_32px")

    consist = AutomobileCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=22560,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCarSymmetric, chassis="2_axle_filled_greebled_24px")

    consist = AutomobileCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24760,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCarSymmetric, chassis="4_axle_filled_greebled_32px")
