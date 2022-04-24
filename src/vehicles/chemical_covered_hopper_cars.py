from train import CoveredHopperCarChemicalConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=6570,
        gen=2,
        subtype="U",
        base_track_type="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=6580,
        gen=3,
        subtype="U",
        base_track_type="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=6590,
        gen=4,
        subtype="U",
        base_track_type="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=6110,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=6040,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=6050,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=6060,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=6070,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=6080,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_half_filled_greebled_32px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=6090,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=6100,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")
