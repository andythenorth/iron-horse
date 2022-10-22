from train import AutomobileCarConsist, AutomobileCarSymmetric


def main():
    # --------------- pony ----------------------------------------------------------------------
    # no gen 1 or 2, straight to gen 3
    """
    consist = AutomobileCarConsist(
        roster_id="pony",
        base_numeric_id=14790,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCarSymmetric, chassis="3_axle_solid_express_24px")
    """
    consist = AutomobileCarConsist(
        roster_id="pony",
        base_numeric_id=14800,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCarSymmetric, chassis="4_axle_solid_express_32px")
    """
    consist = AutomobileCarConsist(
        roster_id="pony",
        base_numeric_id=14780,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCarSymmetric, chassis="4_axle_solid_express_24px")
    """
    consist = AutomobileCarConsist(
        roster_id="pony",
        base_numeric_id=14770,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCarSymmetric, chassis="4_axle_solid_express_32px")
    """
    consist = AutomobileCarConsist(
        roster_id="pony",
        base_numeric_id=14750,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCarSymmetric, chassis="4_axle_filled_greebled_24px")
    """
    consist = AutomobileCarConsist(
        roster_id="pony",
        base_numeric_id=14760,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCarSymmetric, chassis="4_axle_filled_greebled_32px")
    """
    consist = AutomobileCarConsist(
        roster_id="pony",
        base_numeric_id=14810,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCarSymmetric, chassis="4_axle_filled_greebled_24px")
    """
    consist = AutomobileCarConsist(
        roster_id="pony",
        base_numeric_id=14820,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCarSymmetric, chassis="4_axle_filled_greebled_32px")
