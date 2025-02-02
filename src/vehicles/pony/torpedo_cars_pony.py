from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="TorpedoCarConsist",
        base_numeric_id=4140,
        gen=2,
        subtype="U",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="TorpedoCar", vehicle_length=3)

    consist_factory.define_unit(class_name="TorpedoCar", vehicle_length=6)

    consist_factory.define_unit(class_name="TorpedoCar", vehicle_length=3)

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TorpedoCarConsist",
        base_numeric_id=4060,
        gen=3,
        subtype="U",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="TorpedoCar", vehicle_length=3)

    consist_factory.define_unit(class_name="TorpedoCar", vehicle_length=6)

    consist_factory.define_unit(class_name="TorpedoCar", vehicle_length=3)

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TorpedoCarConsist",
        base_numeric_id=4170,
        gen=4,
        subtype="U",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="TorpedoCar", vehicle_length=3)

    consist_factory.define_unit(class_name="TorpedoCar", vehicle_length=6)

    consist_factory.define_unit(class_name="TorpedoCar", vehicle_length=3)

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TorpedoCarConsist",
        base_numeric_id=4090,
        gen=5,
        subtype="U",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="TorpedoCar", vehicle_length=3)

    consist_factory.define_unit(class_name="TorpedoCar", vehicle_length=6)

    consist_factory.define_unit(class_name="TorpedoCar", vehicle_length=3)

    result.append(consist_factory)

    return result
