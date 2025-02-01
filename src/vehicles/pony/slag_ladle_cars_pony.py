from train import SlagLadleCarConsist, SlagLadleCar


def main(roster_id, **kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    consist_factory = SlagLadleCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24030,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, don't spill molten slag eh?
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="SlagLadleCar", chassis="buffers_only_16px")

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = SlagLadleCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23410,
        gen=1,
        subtype="U",
        speed=35,  # note rare non-standard speed, don't spill molten slag eh?
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="SlagLadleCar", chassis="buffers_only_16px")

    result.append(consist_factory)

    consist_factory = SlagLadleCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23420,
        gen=4,
        subtype="U",
        speed=35,  # note rare non-standard speed, don't spill molten slag eh?
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="SlagLadleCar", chassis="buffers_only_16px")

    result.append(consist_factory)

    return result
