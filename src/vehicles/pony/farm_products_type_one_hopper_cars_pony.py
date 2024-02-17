from train import FarmProductsTypeOneHopperCarConsist, FreightCar


def main(roster_id):
    # --------------- standard gauge ---------------------------------------------------------------

    consist = FarmProductsTypeOneHopperCarConsist(
        roster_id=roster_id,
        base_numeric_id=11890,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = FarmProductsTypeOneHopperCarConsist(
        roster_id=roster_id,
        base_numeric_id=13320,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = FarmProductsTypeOneHopperCarConsist(
        roster_id=roster_id,
        base_numeric_id=11910,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = FarmProductsTypeOneHopperCarConsist(
        roster_id=roster_id,
        base_numeric_id=9750,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = FarmProductsTypeOneHopperCarConsist(
        roster_id=roster_id,
        base_numeric_id=11120,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = FarmProductsTypeOneHopperCarConsist(
        roster_id=roster_id,
        base_numeric_id=11710,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = FarmProductsTypeOneHopperCarConsist(
        roster_id=roster_id,
        base_numeric_id=11840,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")

    consist = FarmProductsTypeOneHopperCarConsist(
        roster_id=roster_id,
        base_numeric_id=11730,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_32px")
