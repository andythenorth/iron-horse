from train import DumpCarOreConsist, OreDumpCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    consist = DumpCarOreConsist(
        roster_id="pony",
        base_numeric_id=6490,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=OreDumpCar, chassis="2_axle_gapped_16px")

    consist = DumpCarOreConsist(
        roster_id="pony",
        base_numeric_id=6500,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=OreDumpCar, chassis="4_axle_gapped_24px")

    consist = DumpCarOreConsist(
        roster_id="pony",
        base_numeric_id=6510,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=OreDumpCar, chassis="2_axle_gapped_16px")

    consist = DumpCarOreConsist(
        roster_id="pony",
        base_numeric_id=6520,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=OreDumpCar, chassis="4_axle_sparse_24px")

    # no gen 5A or 6A

    consist = DumpCarOreConsist(
        roster_id="pony",
        base_numeric_id=6530,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=OreDumpCar, chassis="4_axle_sparse_24px")

    consist = DumpCarOreConsist(
        roster_id="pony",
        base_numeric_id=6540,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=OreDumpCar, chassis="4_axle_sparse_32px")

    consist = DumpCarOreConsist(
        roster_id="pony",
        base_numeric_id=6550,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=OreDumpCar, chassis="4_axle_sparse_greebled_24px")

    consist = DumpCarOreConsist(
        roster_id="pony",
        base_numeric_id=6560,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=OreDumpCar, chassis="4_axle_sparse_greebled_32px")
