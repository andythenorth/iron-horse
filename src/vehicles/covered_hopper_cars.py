from train import CoveredHopperCarConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=15020,
        gen=2,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=17880,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=17860,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------
    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=15960,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=11740,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=12900,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=14780,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=13410,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=14120,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")
