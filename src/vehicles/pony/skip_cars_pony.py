from train import HopperCarSkipConsist, FreightCar


def main(roster_id, **kwargs):
    # --------------- narrow gauge -----------------------------------------------------------------

    consist = HopperCarSkipConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=6120,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, skips are slow eh?
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_8px", repeat=2)

    # consist.add_unit(type=FreightCar, chassis="empty_8px")
