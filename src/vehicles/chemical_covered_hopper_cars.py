from train import CoveredHopperCarChemicalConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=15610,
        gen=2,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=15620,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=15630,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=15150,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=15080,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=15090,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=15100,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=15110,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=15120,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_half_filled_greebled_32px")
