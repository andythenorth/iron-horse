from train import GasTankCarCryoConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    consist = GasTankCarCryoConsist(
        roster_id="pony", base_numeric_id=20, gen=4, subtype="A", sprites_complete=False
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = GasTankCarCryoConsist(
        roster_id="pony", base_numeric_id=50, gen=4, subtype="B", sprites_complete=False
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = GasTankCarCryoConsist(
        roster_id="pony", base_numeric_id=60, gen=4, subtype="C", sprites_complete=False
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_32px")

    consist = GasTankCarCryoConsist(
        roster_id="pony", base_numeric_id=6270, gen=5, subtype="A", sprites_complete=False
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = GasTankCarCryoConsist(
        roster_id="pony", base_numeric_id=90, gen=5, subtype="B", sprites_complete=False
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = GasTankCarCryoConsist(
        roster_id="pony", base_numeric_id=150, gen=5, subtype="C", sprites_complete=False
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_32px")

    consist = GasTankCarCryoConsist(
        roster_id="pony", base_numeric_id=6260, gen=6, subtype="A", sprites_complete=False
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = GasTankCarCryoConsist(
        roster_id="pony", base_numeric_id=190, gen=6, subtype="B", sprites_complete=False
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = GasTankCarCryoConsist(
        roster_id="pony", base_numeric_id=200, gen=6, subtype="C", sprites_complete=False
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_32px")
