from train import TankCarAcidConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=6130,
        gen=2,
        subtype="A",
        intro_date_offset=-10,  # let's be earlier for this one
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=6140,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="3_axle_filled_16px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=6150,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=6170,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=6180,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_24px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=6300,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_32px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=6310,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_alt_16px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=6320,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_24px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=6330,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_32px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=6160,
        gen=6,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_alt_16px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=6340,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_24px")

    consist = TankCarAcidConsist(
        roster_id="pony",
        base_numeric_id=6350,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_32px")
