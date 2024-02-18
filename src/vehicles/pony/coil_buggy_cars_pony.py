from train import CoilBuggyCarConsist, CoilBuggyCar


def main(roster_id, **kwargs):
    # --------------- narrow gauge -----------------------------------------------------------------

    consist = CoilBuggyCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=5160,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, don't spill coils eh?
        sprites_complete=True,
    )

    consist.add_unit(type=CoilBuggyCar, chassis="empty_8px", repeat=2)
