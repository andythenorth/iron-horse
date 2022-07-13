from train import IngotCarConsist, IngotCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------

    consist = IngotCarConsist(
        roster_id="pony",
        base_numeric_id=5150,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    consist.add_unit(type=IngotCar, chassis="empty_8px", repeat=2)
