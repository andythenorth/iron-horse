from train import OpenCarRandomisedConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = OpenCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7930,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    # no new type A for gen 2, gen 1 type A continues

    consist = OpenCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7940,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = OpenCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7950,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = OpenCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7960,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = OpenCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7970,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = OpenCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=7980,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = OpenCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8000,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = OpenCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8010,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")

    consist = OpenCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8020,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = OpenCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8030,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")
