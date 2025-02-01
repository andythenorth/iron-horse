from train import ConsistFactory


def main(roster_id, **kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="HopperCarSkipConsist",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=6120,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, skips are slow eh?
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_8px", repeat=2)

    # consist_factory.add_unit(class_name="FreightCar", chassis="empty_8px")

    result.append(consist_factory)

    return result
