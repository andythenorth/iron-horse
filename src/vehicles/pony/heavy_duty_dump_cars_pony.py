from train import BulkOpenCarHeavyDutyConsist


def main(roster_id, **kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    consist_factory = BulkOpenCarHeavyDutyConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17110,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, don't spill heavy things eh?
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="HeavyDutyCar", chassis="4_axle_ng_16px")

    # --------------- pony -------------------------------------------------------------------------

    consist_factory = BulkOpenCarHeavyDutyConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17120,
        gen=1,
        subtype="A",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="HeavyDutyCar", chassis="4_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = BulkOpenCarHeavyDutyConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=16630,
        gen=2,
        subtype="B",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="HeavyDutyCar", chassis="4_axle_filled_24px")

    result.append(consist_factory)

    consist_factory = BulkOpenCarHeavyDutyConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=16530,
        gen=4,
        subtype="A",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="HeavyDutyCar", chassis="4_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = BulkOpenCarHeavyDutyConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30640,
        gen=4,
        subtype="B",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="HeavyDutyCar", chassis="4_axle_filled_24px")

    result.append(consist_factory)

    return result
