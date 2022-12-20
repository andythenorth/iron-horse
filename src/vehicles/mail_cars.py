from train import MailCarConsist, ExpressMailCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------
    consist = MailCarConsist(
        roster_id="pony",
        base_numeric_id=9990,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_ng_16px")

    # no gen 2 for NG, straight to gen 3

    consist = MailCarConsist(
        roster_id="pony",
        base_numeric_id=9650,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_ng_16px")

    consist = MailCarConsist(
        roster_id="pony",
        base_numeric_id=9710,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------

    consist = MailCarConsist(
        roster_id="pony",
        base_numeric_id=11320,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="3_axle_solid_express_16px")

    consist = MailCarConsist(
        roster_id="pony",
        base_numeric_id=11260,
        gen=1,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_24px")

    consist = MailCarConsist(
        roster_id="pony",
        base_numeric_id=11330,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="3_axle_solid_express_16px")

    consist = MailCarConsist(
        roster_id="pony",
        base_numeric_id=9960,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_24px")

    consist = MailCarConsist(
        roster_id="pony",
        base_numeric_id=10870,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="3_axle_solid_express_16px")

    consist = MailCarConsist(
        roster_id="pony",
        base_numeric_id=11340,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_24px")

    consist = MailCarConsist(
        roster_id="pony",
        base_numeric_id=9980,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_32px")

    consist = MailCarConsist(
        roster_id="pony",
        base_numeric_id=10470,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="2_axle_solid_express_16px")

    consist = MailCarConsist(
        roster_id="pony",
        base_numeric_id=12200,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_24px")

    consist = MailCarConsist(
        roster_id="pony",
        base_numeric_id=12210,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_32px")

    consist = MailCarConsist(
        roster_id="pony",
        base_numeric_id=9560,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="2_axle_solid_express_16px")

    consist = MailCarConsist(
        roster_id="pony",
        base_numeric_id=10010,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_24px")

    consist = MailCarConsist(
        roster_id="pony",
        base_numeric_id=12180,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_32px")

    # gen 6 broadly same as gen 5, but new liveries (any other difference?)

    consist = MailCarConsist(
        roster_id="pony",
        base_numeric_id=9910,
        gen=6,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=ExpressMailCar, chassis="2_axle_solid_express_16px")

    consist = MailCarConsist(
        roster_id="pony",
        base_numeric_id=10990,
        gen=6,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_24px")

    consist = MailCarConsist(
        roster_id="pony",
        base_numeric_id=9050,
        gen=6,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_32px")
