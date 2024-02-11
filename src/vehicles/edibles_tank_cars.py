from train import EdiblesTankCarConsist, ExpressCar, FreightCar


def main():

    # --------------- pony NG ----------------------------------------------------------------------

    # note that NG uses FreightCar not ExpressCar, as there is no adjustment of capacity for higher speed
    # this is a bit of an inconsistency in the set design, but it's a tradeoff where the alternative is having no NG edibles tanker at all, or bizarrely low capacity

    consist = EdiblesTankCarConsist(
        roster_id="pony",
        base_numeric_id=19960,
        gen=2,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = EdiblesTankCarConsist(
        roster_id="pony",
        base_numeric_id=19980,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = EdiblesTankCarConsist(
        roster_id="pony",
        base_numeric_id=20000,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_24px")

    # --------------- pony ----------------------------------------------------------------------

    # no gen 1 for edibles tank cars - straight to gen 2

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
