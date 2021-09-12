from train import HopperCarSkipConsist, FreightCar

def main():
    # --------------- pony NG ----------------------------------------------------------------------

    consist = HopperCarSkipConsist(
        roster_id="pony",
        base_numeric_id=6120,
        gen=1,
        subtype="U",
        base_track_type="NG",
        speed=35,  # note rare non-standard speed, skips are slow eh?
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_8px")

    consist.add_unit(type=FreightCar, chassis="empty_8px")
