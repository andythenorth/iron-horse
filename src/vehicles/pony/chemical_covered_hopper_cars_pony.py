from train import CoveredHopperCarChemicalConsist, FreightCar


def main():
    # --------------- narrow gauge -----------------------------------------------------------------

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=14250,
        gen=2,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=14300,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=13150,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_24px")

    # --------------- standard gauge ---------------------------------------------------------------

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=13170,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=10950,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=12700,
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
        base_numeric_id=17340,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_16px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=11000,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")

    consist = CoveredHopperCarChemicalConsist(
        roster_id="pony",
        base_numeric_id=10060,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_half_filled_greebled_32px")
