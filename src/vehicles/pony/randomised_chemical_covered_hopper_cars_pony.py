from train import CoveredHopperCarChemicalRandomisedConsist, FreightCar


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------

    consist = CoveredHopperCarChemicalRandomisedConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24310,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = CoveredHopperCarChemicalRandomisedConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24340,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")
