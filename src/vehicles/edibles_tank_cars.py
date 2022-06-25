from train import EdiblesTankCarConsist, ExpressCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    # no gen 1 or 2 for edibles tank cars - straight to gen 3

    consist = EdiblesTankCarConsist(
        roster_id="pony",
        base_numeric_id=12070,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="2_axle_filled_16px")

    consist = EdiblesTankCarConsist(
        roster_id="pony",
        base_numeric_id=10230,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="3_axle_filled_16px")

    consist = EdiblesTankCarConsist(
        roster_id="pony",
        base_numeric_id=12030,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="3_axle_filled_16px")

    consist = EdiblesTankCarConsist(
        roster_id="pony",
        base_numeric_id=10730,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="4_axle_sparse_24px")

    consist = EdiblesTankCarConsist(
        roster_id="pony",
        base_numeric_id=10260,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="4_axle_sparse_32px")

    consist = EdiblesTankCarConsist(
        roster_id="pony",
        base_numeric_id=10250,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="3_axle_filled_16px")

    consist = EdiblesTankCarConsist(
        roster_id="pony",
        base_numeric_id=10740,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="4_axle_sparse_24px")

    consist = EdiblesTankCarConsist(
        roster_id="pony",
        base_numeric_id=12090,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="4_axle_sparse_32px")

    # gen 6A not included - could add?

    consist = EdiblesTankCarConsist(
        roster_id="pony",
        base_numeric_id=11140,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="4_axle_sparse_24px")

    consist = EdiblesTankCarConsist(
        roster_id="pony",
        base_numeric_id=11130,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="4_axle_sparse_32px")
