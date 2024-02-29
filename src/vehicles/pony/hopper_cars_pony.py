from train import HopperCarConsist, FreightCar


def main(roster_id, **kwargs):
    # --------------- narrow gauge -----------------------------------------------------------------

    consist = HopperCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19810,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = HopperCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19830,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = HopperCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19850,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_24px")

    # --------------- standard gauge ---------------------------------------------------------------

    # just type A for gen 1, 2 and 3

    consist = HopperCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19390,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    # gen 1A also covers gen 2

    consist = HopperCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19410,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = HopperCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19430,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = HopperCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19450,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = HopperCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19470,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = HopperCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19490,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = HopperCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19510,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_16px")

    consist = HopperCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19530,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")

    consist = HopperCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19550,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_32px")
