from train import DumpCarHighSideConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    consist = DumpCarHighSideConsist(
        roster_id="pony",
        base_numeric_id=15760,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = DumpCarHighSideConsist(
        roster_id="pony",
        base_numeric_id=12900,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = DumpCarHighSideConsist(
        roster_id="pony",
        base_numeric_id=12910,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_24px")

    consist = DumpCarHighSideConsist(
        roster_id="pony",
        base_numeric_id=12820,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = DumpCarHighSideConsist(
        roster_id="pony",
        base_numeric_id=12830,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = DumpCarHighSideConsist(
        roster_id="pony",
        base_numeric_id=15750,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_16px")

    consist = DumpCarHighSideConsist(
        roster_id="pony",
        base_numeric_id=12850,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_greebled_24px")

    consist = DumpCarHighSideConsist(
        roster_id="pony",
        base_numeric_id=12860,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_greebled_32px")

    consist = DumpCarHighSideConsist(
        roster_id="pony",
        base_numeric_id=12880,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_24px")

    consist = DumpCarHighSideConsist(
        roster_id="pony",
        base_numeric_id=12890,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_32px")
