from train import DedicatedCoilCarRandomisedConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    consist = DedicatedCoilCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=10710,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = DedicatedCoilCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=10720,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = DedicatedCoilCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=12880,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="empty_32px",
    )

    consist = DedicatedCoilCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=12890,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = DedicatedCoilCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=12950,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")
