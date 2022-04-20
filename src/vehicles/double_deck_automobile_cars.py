from train import AutomobileDoubleDeckCarConsist, AutomobileCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    # intro gen 4

    consist = AutomobileDoubleDeckCarConsist(
        roster_id="pony",
        base_numeric_id=5790,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=AutomobileCar, chassis="2_axle_running_gear_only_24px")

    consist = AutomobileDoubleDeckCarConsist(
        roster_id="pony",
        base_numeric_id=5800,
        gen=4,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=AutomobileCar, chassis="4_axle_running_gear_only_32px")

    consist = AutomobileDoubleDeckCarConsist(
        roster_id="pony",
        base_numeric_id=5810,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=AutomobileCar, chassis="2_axle_running_gear_only_24px")

    consist = AutomobileDoubleDeckCarConsist(
        roster_id="pony",
        base_numeric_id=5820,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=AutomobileCar, chassis="4_axle_running_gear_only_32px")

    consist = AutomobileDoubleDeckCarConsist(
        roster_id="pony",
        base_numeric_id=5840,
        gen=6,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=AutomobileCar, chassis="4_axle_running_gear_only_32px")

    """
    consist = AutomobileDoubleDeckCarConsist(
        roster_id="pony",
        base_numeric_id=5830,
        gen=6,
        subtype="D",
        sprites_complete=False,
    )

    consist.add_unit(
        type=AutomobileCar,
        vehicle_length=5,
        spriterow_num=0,
    )

    consist.add_unit(
        type=AutomobileCar,
        vehicle_length=5,
        spriterow_num=1,
    )
    """
