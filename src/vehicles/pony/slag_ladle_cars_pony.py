from train import SlagLadleCarConsist, SlagLadleCar


def main(roster_id, **kwargs):
    # --------------- narrow gauge -----------------------------------------------------------------

    consist = SlagLadleCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
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
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=13070,
        gen=1,
        subtype="U",
        speed=35,  # note rare non-standard speed, don't spill molten slag eh?
        sprites_complete=True,
    )

    consist.add_unit(type=SlagLadleCar, chassis="buffers_only_16px")

    consist = SlagLadleCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=13080,
        gen=4,
        subtype="U",
        speed=35,  # note rare non-standard speed, don't spill molten slag eh?
        sprites_complete=True,
    )

    consist.add_unit(type=SlagLadleCar, chassis="buffers_only_16px")
