from train import FlatCarHeavyDutyConsist, HeavyDutyCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------

    consist = FlatCarHeavyDutyConsist(
        roster_id="pony",
        base_numeric_id=13580,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, don't spill heavy things eh?
        sprites_complete=True,
    )

    consist.add_unit(type=HeavyDutyCar, chassis="4_axle_ng_16px")

    # --------------- pony -------------------------------------------------------------------------

    consist = FlatCarHeavyDutyConsist(
        roster_id="pony",
        base_numeric_id=10020,
        gen=1,
        subtype="A",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    consist.add_unit(type=HeavyDutyCar, chassis="4_axle_filled_16px")

    consist = FlatCarHeavyDutyConsist(
        roster_id="pony",
        base_numeric_id=10240,
        gen=2,
        subtype="B",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    consist.add_unit(type=HeavyDutyCar, chassis="4_axle_filled_24px")

    consist = FlatCarHeavyDutyConsist(
        roster_id="pony",
        base_numeric_id=10160,
        gen=4,
        subtype="A",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    consist.add_unit(type=HeavyDutyCar, chassis="4_axle_filled_16px")

    consist = FlatCarHeavyDutyConsist(
        roster_id="pony",
        base_numeric_id=10220,
        gen=4,
        subtype="B",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    consist.add_unit(type=HeavyDutyCar, chassis="4_axle_filled_24px")
