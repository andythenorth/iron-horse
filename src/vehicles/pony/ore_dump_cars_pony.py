from train import DumpCarOreConsist, OreDumpCar


def main(roster_id):
    # --------------- standard gauge ---------------------------------------------------------------

    consist = DumpCarOreConsist(
        roster_id=roster_id,
        base_numeric_id=15530,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=OreDumpCar, chassis="2_axle_gapped_16px")

    consist = DumpCarOreConsist(
        roster_id=roster_id,
        base_numeric_id=15540,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=OreDumpCar, chassis="4_axle_gapped_24px")

    consist = DumpCarOreConsist(
        roster_id=roster_id,
        base_numeric_id=15550,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=OreDumpCar, chassis="2_axle_gapped_16px")

    consist = DumpCarOreConsist(
        roster_id=roster_id,
        base_numeric_id=15560,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=OreDumpCar, chassis="4_axle_sparse_24px")

    # no gen 5A or 6A

    consist = DumpCarOreConsist(
        roster_id=roster_id,
        base_numeric_id=15570,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=OreDumpCar, chassis="4_axle_sparse_24px")

    consist = DumpCarOreConsist(
        roster_id=roster_id,
        base_numeric_id=15580,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=OreDumpCar, chassis="4_axle_sparse_32px")
