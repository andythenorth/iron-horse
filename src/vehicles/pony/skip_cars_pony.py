from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="HopperCarSkipConsist",
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
