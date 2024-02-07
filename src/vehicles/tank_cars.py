from train import TankCarConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=17740,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # no gen 2 for NG, straight to gen 3

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=17760,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    """ # restore in next version
    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=17780,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")
    """
    # --------------- pony ----------------------------------------------------------------------

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=17700,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=16360,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=17300,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=14890,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=15710,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_32px")

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=17720,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=13620,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=17680,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_32px")

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=15450,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=11460,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=10670,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_32px")
