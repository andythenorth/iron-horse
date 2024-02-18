from train import ExpressIntermodalCarConsist, ExpressIntermodalCar


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------
    # only gen 5 and 6 eh

    consist = ExpressIntermodalCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=12960,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressIntermodalCar, chassis="2_axle_1cc_filled_24px")

    consist = ExpressIntermodalCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=12970,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressIntermodalCar, chassis="4_axle_1cc_filled_32px")
