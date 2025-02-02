from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="PeatCarConsist",
        base_numeric_id=15170,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, bins are slow eh?
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="BinCar", chassis="empty_8px")

    consist_factory.define_unit(class_name="BinCar", chassis="empty_8px")

    result.append(consist_factory)

    return result
