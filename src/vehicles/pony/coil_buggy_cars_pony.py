from train import CoilBuggyCarConsist, CoilBuggyCar


def main(roster_id, **kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    consist_factory = CoilBuggyCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=5160,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, don't spill coils eh?
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name=CoilBuggyCar, chassis="empty_8px", repeat=2)

    result.append(consist_factory)

    return result
