from train import FarmProductsTypeTwoHopperCarConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = FarmProductsTypeTwoHopperCarConsist(
        roster_id="pony",
        base_numeric_id=15150,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = FarmProductsTypeTwoHopperCarConsist(
        roster_id="pony",
        base_numeric_id=13060,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = FarmProductsTypeTwoHopperCarConsist(
        roster_id="pony",
        base_numeric_id=15300,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = FarmProductsTypeTwoHopperCarConsist(
        roster_id="pony",
        base_numeric_id=11760,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = FarmProductsTypeTwoHopperCarConsist(
        roster_id="pony",
        base_numeric_id=17990,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = FarmProductsTypeTwoHopperCarConsist(
        roster_id="pony",
        base_numeric_id=17460,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = FarmProductsTypeTwoHopperCarConsist(
        roster_id="pony",
        base_numeric_id=17980,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")

    consist = FarmProductsTypeTwoHopperCarConsist(
        roster_id="pony",
        base_numeric_id=16620,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_32px")
