from train import CoveredHopperCarConsistType1, FreightCar


def main(roster_id, **kwargs):
    # --------------- narrow gauge -----------------------------------------------------------------

    consist = CoveredHopperCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=27880,
        gen=2,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = CoveredHopperCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17880,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = CoveredHopperCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23750,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_24px")

    # --------------- standard gauge ---------------------------------------------------------------

    consist = CoveredHopperCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23780,
        gen=2,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23800,
        gen=3,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23820,
        gen=4,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23840,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = CoveredHopperCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23860,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_chute_greebled_24px")

    consist = CoveredHopperCarConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23880,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_chute_greebled_alt_32px")
