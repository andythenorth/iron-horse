from train import ExpressIntermodalCarConsist, ExpressIntermodalCar


def main(roster_id, **kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # only gen 5 and 6 eh

    consist_factory = ExpressIntermodalCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=22960,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=ExpressIntermodalCar, chassis="2_axle_1cc_filled_24px")

    result.append(consist_factory)

    consist_factory = ExpressIntermodalCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=22970,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=ExpressIntermodalCar, chassis="4_axle_1cc_filled_32px")

    result.append(consist_factory)

    return result
