from train import CaneBinCarConsist, BinCar


def main(roster_id, **kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------


    consist_factory = CaneBinCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=1020,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, bins are slow eh?
        sprites_complete=True,
    )

    consist_factory.add_unit(type=BinCar, chassis="empty_8px")

    consist_factory.add_unit(type=BinCar, chassis="empty_8px")

    result.append(consist_factory)

    return result
