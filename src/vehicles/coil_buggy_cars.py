from train import CoilBuggyCarConsist, CoilBuggyCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------

    consist = CoilBuggyCarConsist(
        roster_id="pony",
        base_numeric_id=5160,
        gen=1,
        subtype="U",
        base_track_type="NG",
        speed=35,  # note rare non-standard speed, don't spill coils eh?
        sprites_complete=True,
    )

    consist.add_unit(type=CoilBuggyCar, chassis="buffers_only_ng_8px")

    consist.add_unit(type=CoilBuggyCar, chassis="buffers_only_ng_8px")
