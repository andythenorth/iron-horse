from train import SiloCarChemicalConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = SiloCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=15450,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = SiloCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=15460,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_24px")

    consist = SiloCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=15900,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    consist = SiloCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=15910,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_16px")

    consist = SiloCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=15920,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_24px")

    consist = SiloCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=15930,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    consist = SiloCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=15940,
        gen=6,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = SiloCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=17300,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_24px")

    consist = SiloCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=17310,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")
