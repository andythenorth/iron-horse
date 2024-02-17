from train import SlagLadleCarConsist, SlagLadleCar


def main():
    # --------------- narrow gauge -----------------------------------------------------------------

    consist = SlagLadleCarConsist(
        roster_id="pony",
        base_numeric_id=13480,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, don't spill molten slag eh?
        sprites_complete=True,
    )

    consist.add_unit(type=SlagLadleCar, chassis="buffers_only_16px")

    # --------------- standard gauge ---------------------------------------------------------------

    consist = SlagLadleCarConsist(
        roster_id="pony",
        base_numeric_id=13070,
        gen=1,
        subtype="U",
        speed=35,  # note rare non-standard speed, don't spill molten slag eh?
        sprites_complete=True,
    )

    consist.add_unit(type=SlagLadleCar, chassis="buffers_only_16px")

    consist = SlagLadleCarConsist(
        roster_id="pony",
        base_numeric_id=13080,
        gen=4,
        subtype="U",
        speed=35,  # note rare non-standard speed, don't spill molten slag eh?
        sprites_complete=True,
    )

    consist.add_unit(type=SlagLadleCar, chassis="buffers_only_16px")
