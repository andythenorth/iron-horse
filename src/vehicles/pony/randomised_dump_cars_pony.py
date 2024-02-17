from train import DumpCarRandomisedConsist, FreightCar


def main():
    # --------------- narrow gauge -----------------------------------------------------------------

    consist = DumpCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=15750,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = DumpCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=15880,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = DumpCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=10900,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    # --------------- standard gauge ---------------------------------------------------------------

    consist = DumpCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17190,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    # no new type A for gen 2, gen 1 type A continues

    consist = DumpCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17200,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = DumpCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17210,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = DumpCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17220,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = DumpCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17230,
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
        base_numeric_id=8450,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = DumpCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8210,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")
