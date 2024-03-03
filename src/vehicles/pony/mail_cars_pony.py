from train import MailCarConsist, ExpressMailCar


def main(roster_id, **kwargs):
    # --------------- narrow gauge -----------------------------------------------------------------
    consist = MailCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30000,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_ng_16px")

    # no gen 2 for NG, straight to gen 3

    consist = MailCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30010,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_ng_16px")

    consist = MailCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30020,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_ng_24px")

    consist = MailCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=30030,
        gen=4,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_ng_16px")

    consist = MailCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30260,
        gen=4,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_ng_24px")

    # --------------- standard gauge ---------------------------------------------------------------

    consist = MailCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30040,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="3_axle_solid_express_16px")

    consist = MailCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30050,
        gen=1,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_24px")

    consist = MailCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30060,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="3_axle_solid_express_16px")

    consist = MailCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30070,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_24px")

    consist = MailCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30080,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="3_axle_solid_express_16px")

    consist = MailCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30090,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_24px")

    consist = MailCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30100,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_32px")

    consist = MailCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30110,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="2_axle_solid_express_16px")

    consist = MailCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30140,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_24px")

    consist = MailCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30150,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_32px")

    consist = MailCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30160,
        gen=5,
        subtype="A",
        liveries="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="2_axle_solid_express_16px")

    consist = MailCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30170,
        gen=5,
        subtype="B",
        liveries="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_24px")

    consist = MailCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30180,
        gen=5,
        subtype="C",
        liveries="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_32px")
