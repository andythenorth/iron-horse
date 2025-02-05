from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="MineralCoveredHopperCarRandomisedConsist",
        base_numeric_id=26590,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_type_factory)

    # no new type A for gen 2, gen 1 type A continues

    model_type_factory = ModelTypeFactory(
        class_name="MineralCoveredHopperCarRandomisedConsist",
        base_numeric_id=32860,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="MineralCoveredHopperCarRandomisedConsist",
        base_numeric_id=24940,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="MineralCoveredHopperCarRandomisedConsist",
        base_numeric_id=24960,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="MineralCoveredHopperCarRandomisedConsist",
        base_numeric_id=24730,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="MineralCoveredHopperCarRandomisedConsist",
        base_numeric_id=24880,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="MineralCoveredHopperCarRandomisedConsist",
        base_numeric_id=22230,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(model_type_factory)

    return result
