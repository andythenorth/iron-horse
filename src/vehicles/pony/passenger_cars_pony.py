from train import PassengerCarConsist, PaxCar


def main(roster_id, **kwargs):
    # --------------- narrow gauge -----------------------------------------------------------------
    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=9810,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_16px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=10570,
        gen=1,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_24px")

    # no gen 2 for NG, straight to gen 3

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=9840,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_16px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=9640,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_24px")

    """ # restore in next version
    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=9900,
        gen=4,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_16px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=9700,
        gen=4,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_24px")
    """
    # --------------- standard gauge ---------------------------------------------------------------

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=14620,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="2_axle_solid_express_16px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=14630,
        gen=1,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_24px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=11290,
        gen=1,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="6_axle_solid_express_32px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=14640,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="2_axle_solid_express_16px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=14650,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_24px")
    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=11300,
        gen=2,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="6_axle_solid_express_32px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=14660,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="3_axle_solid_express_16px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=14670,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_24px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=11310,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_32px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=14680,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_24px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=12160,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_32px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=9780,
        gen=5,
        subtype="B",
        liveries="gen_5_and_6_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_24px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=12170,
        gen=5,
        subtype="C",
        liveries="gen_5_and_6_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_32px")
