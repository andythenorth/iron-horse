from train import CaneBinCarConsist, BinCar


def main(roster_id, **kwargs):
    # --------------- narrow gauge -----------------------------------------------------------------


    consist = CaneBinCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=1020,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, bins are slow eh?
        sprites_complete=True,
    )

    consist.add_unit(type=BinCar, chassis="empty_8px")

    consist.add_unit(type=BinCar, chassis="empty_8px")

