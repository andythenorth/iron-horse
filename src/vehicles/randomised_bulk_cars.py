from train import BulkCarRandomisedConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------

    print(
        "CABBAGE 4400, all ng randomised bulk cars nerfed off as they need variants reworked (so ore brown is a remap variant, not drawn etc)"
    )

    """

    consist = BulkCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8340,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = BulkCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16920,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = BulkCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17030,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")
    """
    # --------------- pony ----------------------------------------------------------------------

    consist = BulkCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8240,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    # no new type A for gen 2, gen 1 type A continues

    consist = BulkCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8250,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = BulkCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8260,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = BulkCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8270,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = BulkCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8280,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = BulkCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8290,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = BulkCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8300,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")
