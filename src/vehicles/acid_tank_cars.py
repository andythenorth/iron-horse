from train import TankCarAcidConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=15170,
        gen=2,
        subtype="A",
        intro_date_offset=-10,  # let's be earlier for this one
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=15180,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="3_axle_filled_16px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=15190,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=15210,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=15220,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_24px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=15340,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_32px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=15350,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_alt_16px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=15360,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_24px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=15370,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_32px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=15200,
        gen=6,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_alt_16px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=15380,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_24px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=15390,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_32px")
