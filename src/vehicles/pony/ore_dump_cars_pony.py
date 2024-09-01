from train import BulkOpenCarOreConsist, OreDumpCar


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------

    consist = BulkOpenCarOreConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35530,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=OreDumpCar, chassis="2_axle_gapped_16px")

    consist = BulkOpenCarOreConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35540,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=OreDumpCar, chassis="4_axle_gapped_24px")

    consist = BulkOpenCarOreConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35550,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=OreDumpCar, chassis="2_axle_gapped_16px")

    consist = BulkOpenCarOreConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35560,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=OreDumpCar, chassis="4_axle_sparse_24px")

    # no gen 5A or 6A

    consist = BulkOpenCarOreConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35570,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=OreDumpCar, chassis="4_axle_sparse_24px")

    consist = BulkOpenCarOreConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35580,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=OreDumpCar, chassis="4_axle_sparse_32px")
