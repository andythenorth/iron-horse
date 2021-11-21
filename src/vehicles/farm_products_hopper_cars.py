from train import FarmProductsHopperCarConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    consist = FarmProductsHopperCarConsist(
        roster_id="pony",
        base_numeric_id=2850,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = FarmProductsHopperCarConsist(
        roster_id="pony",
        base_numeric_id=2870,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = FarmProductsHopperCarConsist(
        roster_id="pony",
        base_numeric_id=2080,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = FarmProductsHopperCarConsist(
        roster_id="pony",
        base_numeric_id=2670,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = FarmProductsHopperCarConsist(
        roster_id="pony",
        base_numeric_id=2800,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = FarmProductsHopperCarConsist(
        roster_id="pony",
        base_numeric_id=2690,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    consist = FarmProductsHopperCarConsist(
        roster_id="pony",
        base_numeric_id=2810,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = FarmProductsHopperCarConsist(
        roster_id="pony",
        base_numeric_id=2820,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")
