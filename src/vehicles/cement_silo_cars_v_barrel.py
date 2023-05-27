from train import SiloCarCementVBarrelConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = SiloCarCementVBarrelConsist(
        roster_id="pony",
        base_numeric_id=13200,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = SiloCarCementVBarrelConsist(
        roster_id="pony",
        base_numeric_id=13210,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_24px")

    consist = SiloCarCementVBarrelConsist(
        roster_id="pony",
        base_numeric_id=13290,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    consist = SiloCarCementVBarrelConsist(
        roster_id="pony",
        base_numeric_id=13300,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_16px")

    consist = SiloCarCementVBarrelConsist(
        roster_id="pony",
        base_numeric_id=13310,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_hopppers_24px")

    consist = SiloCarCementVBarrelConsist(
        roster_id="pony",
        base_numeric_id=13400,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_hoppers_32px")
