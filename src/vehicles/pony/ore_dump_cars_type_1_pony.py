from train import BulkOpenCarOreConsistType1, OreDumpCar


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------

    consist = BulkOpenCarOreConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35530,
        gen=3,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=OreDumpCar, chassis="2_axle_gapped_16px")

    consist = BulkOpenCarOreConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=32240,
        gen=3,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=OreDumpCar, chassis="4_axle_gapped_24px")

    consist = BulkOpenCarOreConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35550,
        gen=4,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=OreDumpCar, chassis="2_axle_gapped_16px")

    consist = BulkOpenCarOreConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=32260,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=OreDumpCar, chassis="4_axle_sparse_24px")

    # no gen 5A or 6A

    consist = BulkOpenCarOreConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35570,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=OreDumpCar, chassis="4_axle_sparse_24px")

    consist = BulkOpenCarOreConsistType1(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=32280,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=OreDumpCar, chassis="4_axle_sparse_32px")
