from train import GasTankCarCryoConsist, FreightCar


def main(roster_id):
    # --------------- standard gauge ---------------------------------------------------------------

    consist = GasTankCarCryoConsist(
        roster_id=roster_id,
        base_numeric_id=9060,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = GasTankCarCryoConsist(
        roster_id=roster_id,
        base_numeric_id=9090,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = GasTankCarCryoConsist(
        roster_id=roster_id,
        base_numeric_id=9100,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_32px")

    consist = GasTankCarCryoConsist(
        roster_id=roster_id,
        base_numeric_id=15310,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_greebled_16px")

    consist = GasTankCarCryoConsist(
        roster_id=roster_id,
        base_numeric_id=9130,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_24px")

    consist = GasTankCarCryoConsist(
        roster_id=roster_id,
        base_numeric_id=9190,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_32px")
