from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    consist_factory = ConsistFactory(
        class_name="MineralCoveredHopperCarRollerRoofRandomisedConsist",
        base_numeric_id=24650,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="MineralCoveredHopperCarRollerRoofRandomisedConsist",
        base_numeric_id=24670,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="MineralCoveredHopperCarRollerRoofRandomisedConsist",
        base_numeric_id=24690,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="MineralCoveredHopperCarRollerRoofRandomisedConsist",
        base_numeric_id=24710,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    return result
