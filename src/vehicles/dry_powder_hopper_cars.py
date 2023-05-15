from train import CoveredHopperCarDryPowderConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------

    consist = CoveredHopperCarDryPowderConsist(
        roster_id="pony",
        base_numeric_id=15020,
        gen=2,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = CoveredHopperCarDryPowderConsist(
        roster_id="pony",
        base_numeric_id=17880,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = CoveredHopperCarDryPowderConsist(
        roster_id="pony",
        base_numeric_id=17860,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------
    consist = CoveredHopperCarDryPowderConsist(
        roster_id="pony",
        base_numeric_id=13540,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarDryPowderConsist(
        roster_id="pony",
        base_numeric_id=17800,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarDryPowderConsist(
        roster_id="pony",
        base_numeric_id=13560,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = CoveredHopperCarDryPowderConsist(
        roster_id="pony",
        base_numeric_id=17820,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    # no gen 5A or 6A

    consist = CoveredHopperCarDryPowderConsist(
        roster_id="pony",
        base_numeric_id=13590,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = CoveredHopperCarDryPowderConsist(
        roster_id="pony",
        base_numeric_id=17840,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")
