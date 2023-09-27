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

    # --------------- pony -------------------------------------------------------------------------

    consist = IngotCarConsist(
        roster_id="pony",
        base_numeric_id=80,
        gen=1,
        subtype="U",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=False,
    )

    consist.add_unit(type=IngotCar, chassis="empty_8px", repeat=2)


    consist = IngotCarConsist(
        roster_id="pony",
        base_numeric_id=60,
        gen=4,
        subtype="U",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=False,
    )

    consist.add_unit(type=IngotCar, chassis="empty_8px", repeat=2)
