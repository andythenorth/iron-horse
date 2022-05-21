from train import DumpCarRandomisedConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = DumpCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8150,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    # no new type A for gen 2, gen 1 type A continues

    consist = DumpCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8160,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = DumpCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8170,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = DumpCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8180,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = DumpCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8190,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = DumpCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8200,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = DumpCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8210,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")

    consist = DumpCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8220,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = DumpCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8230,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")
