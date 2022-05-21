from train import ColdMetalCarRandomisedConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = ColdMetalCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7710,
        gen=1,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    # no new type A for gen 2, gen 1 type A continues

    consist = ColdMetalCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7720,
        gen=2,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = ColdMetalCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7730,
        gen=3,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = ColdMetalCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7740,
        gen=3,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = ColdMetalCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7750,
        gen=4,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = ColdMetalCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7760,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = ColdMetalCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7770,
        gen=4,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=False,  # non-standard roof for this wagon
        chassis="empty_32px",
    )

    consist = ColdMetalCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7780,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = ColdMetalCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7790,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")

    consist = ColdMetalCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7800,
        gen=6,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = ColdMetalCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7810,
        gen=6,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")
