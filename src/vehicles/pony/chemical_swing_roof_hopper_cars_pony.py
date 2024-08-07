from train import CoveredHopperCarSwingRoofChemicalConsist, FreightCar


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------

    consist = CoveredHopperCarSwingRoofChemicalConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=27260,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_1cc_filled_hoppers_24px")

    consist = CoveredHopperCarSwingRoofChemicalConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=22060,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_hoppers_32px")
