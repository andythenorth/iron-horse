from train import FlatCarRandomisedConsist, FreightCar


def main():
    # --------------- pony NG -------------------------------------------------------------------

    consist = FlatCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7830,
        gen=1,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = FlatCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=6910,
        gen=3,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = FlatCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7490,
        gen=4,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    # --------------- pony ----------------------------------------------------------------------

    consist = FlatCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8500,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    # no new type A for gen 2, gen 1 type A continues

    consist = FlatCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8510,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = FlatCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8520,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = FlatCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8530,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = FlatCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8540,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = FlatCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8550,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = FlatCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8560,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="empty_32px",
    )

    consist = FlatCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8570,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = FlatCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8580,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")

    consist = FlatCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8590,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = FlatCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8600,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")
