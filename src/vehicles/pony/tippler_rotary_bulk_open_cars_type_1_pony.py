from train import BulkOpenCarTipplerRotaryConsistType1, OreDumpCar


def main(roster_id, **kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    consist_factory = BulkOpenCarTipplerRotaryConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=26650,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="OreDumpCar", chassis="4_axle_ng_sparse_16px")

    result.append(consist_factory)

    consist_factory = BulkOpenCarTipplerRotaryConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=26670,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="OreDumpCar", chassis="4_axle_ng_sparse_24px")

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = BulkOpenCarTipplerRotaryConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35550,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="OreDumpCar", chassis="2_axle_gapped_16px")

    result.append(consist_factory)

    consist_factory = BulkOpenCarTipplerRotaryConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=32260,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="OreDumpCar", chassis="4_axle_sparse_24px")

    # no gen 5A or 6A

    consist_factory = BulkOpenCarTipplerRotaryConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35570,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="OreDumpCar", chassis="4_axle_sparse_greebled_24px")

    result.append(consist_factory)

    consist_factory = BulkOpenCarTipplerRotaryConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=32280,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="OreDumpCar", chassis="4_axle_sparse_greebled_32px")

    result.append(consist_factory)

    return result
