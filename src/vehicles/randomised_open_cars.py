from train import OpenCarRandomisedConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = OpenCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16970,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    # no new type A for gen 2, gen 1 type A continues

    consist = OpenCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16980,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = OpenCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16990,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = OpenCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17000,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = OpenCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17010,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = OpenCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17020,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = OpenCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17040,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = OpenCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17050,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")

    consist = OpenCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17060,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = OpenCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17070,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")
