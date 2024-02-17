from train import BoxCarRandomisedConsist, FreightCar


def main(roster_id):
    # --------------- standard gauge ---------------------------------------------------------------

    consist = BoxCarRandomisedConsist(
        roster_id=roster_id,
        base_numeric_id=16680,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = BoxCarRandomisedConsist(
        roster_id=roster_id,
        base_numeric_id=16690,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = BoxCarRandomisedConsist(
        roster_id=roster_id,
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
        roster_id=roster_id,
        base_numeric_id=16710,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = BoxCarRandomisedConsist(
        roster_id=roster_id,
        base_numeric_id=16720,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")
