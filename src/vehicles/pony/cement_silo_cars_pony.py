from train import SiloCarCementConsist, FreightCar


def main():
    # --------------- standard gauge ---------------------------------------------------------------

    consist = SiloCarCementConsist(
        roster_id="pony",
        base_numeric_id=10270,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = SiloCarCementConsist(
        roster_id="pony",
        base_numeric_id=10280,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_24px")

    consist = SiloCarCementConsist(
        roster_id="pony",
        base_numeric_id=10300,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    consist = SiloCarCementConsist(
        roster_id="pony",
        base_numeric_id=10310,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_16px")

    consist = SiloCarCementConsist(
        roster_id="pony",
        base_numeric_id=10380,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_hopppers_24px")

    consist = SiloCarCementConsist(
        roster_id="pony",
        base_numeric_id=10980,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_hoppers_32px")
