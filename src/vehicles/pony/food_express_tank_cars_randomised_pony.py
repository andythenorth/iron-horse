from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="ExpressFoodTankCarRandomisedConsist",
        base_numeric_id=28160,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ExpressFoodTankCarRandomisedConsist",
        base_numeric_id=28170,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(consist_factory)

    return result
