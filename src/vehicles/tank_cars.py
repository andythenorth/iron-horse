from train import TankCarConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=9690,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # no gen 2 for NG, straight to gen 3

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=12020,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=9730,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=10240,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=12220,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=9670,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=11470,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=11940,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_32px")

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=9680,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=10000,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=10290,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_32px")

    consist = TankCarConsist(
        roster_id="pony",
        base_numeric_id=11450,
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
        base_numeric_id=11970,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_32px")
