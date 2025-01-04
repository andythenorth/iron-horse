from train import AutomobileCarConsist, AutomobileCarSymmetric


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------    # no gen 1 or 2, straight to gen 3

    consist = AutomobileCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=22540,
        gen=3,
        subtype="B",
        sprites_complete=False,
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
    """
    consist = AutomobileCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=24780,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCarSymmetric, chassis="4_axle_solid_express_24px")
    """
    consist = AutomobileCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24770,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCarSymmetric, chassis="4_axle_solid_express_32px")
    """
    consist = AutomobileCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=24750,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCarSymmetric, chassis="4_axle_filled_greebled_24px")
    """
    consist = AutomobileCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24760,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCarSymmetric, chassis="4_axle_filled_greebled_32px")
