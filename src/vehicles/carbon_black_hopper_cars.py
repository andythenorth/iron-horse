from train import CarbonBlackHopperCarConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = CarbonBlackHopperCarConsist(
        roster_id="pony",
        base_numeric_id=13450,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CarbonBlackHopperCarConsist(
        roster_id="pony",
        base_numeric_id=13460,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = CarbonBlackHopperCarConsist(
        roster_id="pony",
        base_numeric_id=13470,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = CarbonBlackHopperCarConsist(
        roster_id="pony",
        base_numeric_id=13490,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")

    consist = CarbonBlackHopperCarConsist(
        roster_id="pony",
        base_numeric_id=13500,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_32px")
