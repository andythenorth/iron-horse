from train import GenericCoilCarRandomisedConsist, FreightCar


def main():
    # --------------- standard gauge ---------------------------------------------------------------

    consist = GenericCoilCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16750,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    # no new type A for gen 2, gen 1 type A continues

    consist = GenericCoilCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16760,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = GenericCoilCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16770,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = GenericCoilCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16780,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = GenericCoilCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16790,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = GenericCoilCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16800,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = GenericCoilCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16810,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="empty_32px",
    )

    consist = GenericCoilCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16820,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = GenericCoilCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16830,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")
