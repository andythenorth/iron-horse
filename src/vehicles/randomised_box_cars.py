from train import BoxCarRandomisedConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = BoxCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16640,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    # no new type A for gen 2, gen 1 type A continues

    consist = BoxCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16650,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = BoxCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16660,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = BoxCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16670,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = BoxCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16680,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = BoxCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16690,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = BoxCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16700,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="empty_32px",
    )

    consist = BoxCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16710,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = BoxCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16720,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")
