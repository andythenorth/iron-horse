from train import PassengerCarConsist, PaxCar


def main(roster_id, **kwargs):
    # --------------- narrow gauge -----------------------------------------------------------------
    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25330,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        buy_menu_additional_text_role_string="STR_ROLE_GENERAL_PURPOSE",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_16px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24090,
        gen=1,
        subtype="B",
        base_track_type_name="NG",
        buy_menu_additional_text_role_string="STR_ROLE_GENERAL_PURPOSE",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_24px")

    # no gen 2 for NG, straight to gen 3

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25000,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        buy_menu_additional_text_role_string="STR_ROLE_GENERAL_PURPOSE",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_16px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25010,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        buy_menu_additional_text_role_string="STR_ROLE_GENERAL_PURPOSE",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_24px")

    # no gen 4A NG coach

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=34220,
        gen=4,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_24px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=25550,
        gen=4,
        subtype="C",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_32px")

    # --------------- standard gauge ---------------------------------------------------------------

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=34620,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="2_axle_solid_express_16px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=34630,
        gen=1,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_24px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30410,
        gen=1,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="6_axle_solid_express_32px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=34640,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="2_axle_solid_express_16px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=34650,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_24px")
    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30420,
        gen=2,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="6_axle_solid_express_32px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=34660,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="3_axle_solid_express_16px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=34670,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_24px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30430,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_32px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=34680,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_24px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25300,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_32px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25310,
        gen=5,
        subtype="B",
        liveries="gen_5_and_6_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_24px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25320,
        gen=5,
        subtype="C",
        liveries="gen_5_and_6_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_32px")
