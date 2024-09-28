from train import CoveredHopperCarMineralConsistType2, FreightCar


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------
    """
    consist = CoveredHopperCarMineralConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25990,
        gen=2,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarMineralConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=26000,
        gen=3,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")
    """
    consist = CoveredHopperCarMineralConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24900,
        gen=4,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarMineralConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24910,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = CoveredHopperCarMineralConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24920,
        gen=5,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_16px")

    consist = CoveredHopperCarMineralConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24930,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = CoveredHopperCarMineralConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=22250,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_chute_greebled_alt_32px")
