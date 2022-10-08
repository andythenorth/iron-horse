from train import CoveredHopperCarRandomisedConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------

    consist = CoveredHopperCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16620,
        gen=2,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = CoveredHopperCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=16630,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = CoveredHopperCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17280,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------

    # gen 2 start

    consist = CoveredHopperCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17240,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = CoveredHopperCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17250,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = CoveredHopperCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=15830,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = CoveredHopperCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=15840,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = CoveredHopperCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=15860,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = CoveredHopperCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=15870,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")

    consist = CoveredHopperCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=15880,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = CoveredHopperCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=15890,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")
