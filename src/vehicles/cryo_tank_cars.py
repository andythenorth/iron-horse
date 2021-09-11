from train import CryoTankCarConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------

    consist = CryoTankCarConsist(
        roster_id="pony",
        base_numeric_id=6010,
        gen=2,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = CryoTankCarConsist(
        roster_id="pony",
        base_numeric_id=6020,
        gen=3,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = CryoTankCarConsist(
        roster_id="pony",
        base_numeric_id=6030,
        gen=4,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------
    consist = CryoTankCarConsist(
        roster_id="pony", base_numeric_id=80, gen=2, subtype="A", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = CryoTankCarConsist(
        roster_id="pony", base_numeric_id=180, gen=3, subtype="A", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = CryoTankCarConsist(
        roster_id="pony", base_numeric_id=250, gen=3, subtype="B", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = CryoTankCarConsist(
        roster_id="pony", base_numeric_id=20, gen=4, subtype="A", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = CryoTankCarConsist(
        roster_id="pony", base_numeric_id=50, gen=4, subtype="B", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = CryoTankCarConsist(
        roster_id="pony", base_numeric_id=60, gen=4, subtype="C", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_32px")

    # no gen 5A or 6A

    consist = CryoTankCarConsist(
        roster_id="pony", base_numeric_id=90, gen=5, subtype="B", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = CryoTankCarConsist(
        roster_id="pony", base_numeric_id=150, gen=5, subtype="C", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_32px")

    consist = CryoTankCarConsist(
        roster_id="pony", base_numeric_id=190, gen=6, subtype="B", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = CryoTankCarConsist(
        roster_id="pony", base_numeric_id=200, gen=6, subtype="C", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_32px")
