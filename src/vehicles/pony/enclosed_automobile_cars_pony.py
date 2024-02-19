from train import AutomobileEnclosedCarConsist, ExpressCar


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------
    consist = AutomobileEnclosedCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=18000,
        gen=3,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=ExpressCar, chassis="4_axle_solid_express_32px")

    consist = AutomobileEnclosedCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=18010,
        gen=4,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=ExpressCar, chassis="4_axle_solid_express_32px")

    consist = AutomobileEnclosedCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=18060,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=ExpressCar, chassis="4_axle_filled_greebled_32px")
