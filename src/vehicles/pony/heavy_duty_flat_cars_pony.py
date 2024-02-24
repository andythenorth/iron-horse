from train import FlatCarHeavyDutyConsist, HeavyDutyCar


def main(roster_id, **kwargs):
    # --------------- narrow gauge -----------------------------------------------------------------

    consist = FlatCarHeavyDutyConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=21920,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, don't spill heavy things eh?
        sprites_complete=True,
    )

    consist.add_unit(type=HeavyDutyCar, chassis="4_axle_ng_16px")

    # --------------- pony -------------------------------------------------------------------------

    consist = FlatCarHeavyDutyConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=21930,
        gen=1,
        subtype="A",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    consist.add_unit(type=HeavyDutyCar, chassis="4_axle_filled_16px")

    consist = FlatCarHeavyDutyConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=21940,
        gen=2,
        subtype="B",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    consist.add_unit(type=HeavyDutyCar, chassis="4_axle_filled_24px")

    consist = FlatCarHeavyDutyConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=21950,
        gen=4,
        subtype="A",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    consist.add_unit(type=HeavyDutyCar, chassis="4_axle_filled_16px")

    consist = FlatCarHeavyDutyConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=21960,
        gen=4,
        subtype="B",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    consist.add_unit(type=HeavyDutyCar, chassis="4_axle_filled_24px")
