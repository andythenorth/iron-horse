from train import SiloCarConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = SiloCarConsist(
        roster_id="pony",
        base_numeric_id=12720,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = SiloCarConsist(
        roster_id="pony",
        base_numeric_id=17390,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_24px")

    consist = SiloCarConsist(
        roster_id="pony",
        base_numeric_id=17430,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    consist = SiloCarConsist(
        roster_id="pony",
        base_numeric_id=12660,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_16px")

    consist = SiloCarConsist(
        roster_id="pony",
        base_numeric_id=17410,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_hopppers_24px")

    consist = SiloCarConsist(
        roster_id="pony",
        base_numeric_id=12680,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_hoppers_32px")
