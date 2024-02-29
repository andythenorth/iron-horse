from train import HopperCarHighSideConsist, FreightCar


def main(roster_id, **kwargs):
    # --------------- narrow gauge -----------------------------------------------------------------

    consist = HopperCarHighSideConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19750,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = HopperCarHighSideConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19770,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = HopperCarHighSideConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19790,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_24px")

    # --------------- standard gauge ---------------------------------------------------------------
    # also just type A for gen 1, 2 and 3

    consist = HopperCarHighSideConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19570,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    # gen 1A also covers gen 2

    consist = HopperCarHighSideConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19590,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = HopperCarHighSideConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19610,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = HopperCarHighSideConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19630,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = HopperCarHighSideConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19650,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = HopperCarHighSideConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19670,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = HopperCarHighSideConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19690,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = HopperCarHighSideConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19710,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")

    consist = HopperCarHighSideConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19730,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_32px")
