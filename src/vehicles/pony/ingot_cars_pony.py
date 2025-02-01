from train import IngotCarConsist


def main(roster_id, **kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    consist_factory = IngotCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=5150,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="IngotCar", chassis="empty_8px", repeat=2)

    # --------------- pony -------------------------------------------------------------------------

    consist_factory = IngotCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=80,
        gen=1,
        subtype="U",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="IngotCar", chassis="empty_8px", repeat=2)

    result.append(consist_factory)

    consist_factory = IngotCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=60,
        gen=4,
        subtype="U",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="IngotCar", chassis="empty_8px", repeat=2)

    result.append(consist_factory)

    return result
