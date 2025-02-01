from train import ConsistFactory


def main(roster_id, **kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="HopperCarRockConsist",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=27060,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_ng_sparse_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarRockConsist",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=21990,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_ng_sparse_24px")

    result.append(consist_factory)

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="HopperCarRockConsist",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24100,
        gen=4,
        subtype="B",
        intro_year_offset=7,  # let's be a little bit later for this one
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_sparse_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarRockConsist",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24120,
        gen=4,
        subtype="C",
        intro_year_offset=7,  # let's be a little bit later for this one
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_sparse_32px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarRockConsist",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24140,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_sparse_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarRockConsist",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24160,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_sparse_32px")

    result.append(consist_factory)

    return result
