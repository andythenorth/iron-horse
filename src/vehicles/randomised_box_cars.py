from train import BoxCarRandomisedConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = BoxCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7600,
        gen=1,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, vehicle_length=4)

    # no new type A for gen 2, gen 1 type A continues

    consist = BoxCarRandomisedConsist(
        roster_id="pony", base_numeric_id=7610, gen=2, subtype="B", sprites_complete=False
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = BoxCarRandomisedConsist(
        roster_id="pony", base_numeric_id=7620, gen=3, subtype="A", sprites_complete=False
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = BoxCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7630,
        gen=3,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_24px")

    consist = BoxCarRandomisedConsist(
        roster_id="pony", base_numeric_id=7640, gen=4, subtype="A", sprites_complete=False
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = BoxCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7650,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_24px")

    consist = BoxCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7660,
        gen=4,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=False,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    consist = BoxCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7670,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = BoxCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7680,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")

    consist = BoxCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7690,
        gen=6,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = BoxCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7700,
        gen=6,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")
