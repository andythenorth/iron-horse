from train import FlatCarTarpaulinConsist, FreightCar


def main():
    # --------------- ibex ----------------------------------------------------------------------

    # gen 5 start, only B and C lengths

    consist = FlatCarTarpaulinConsist(
        roster_id="ibex",
        base_numeric_id=8810,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_24px")

    consist = FlatCarTarpaulinConsist(
        roster_id="ibex",
        base_numeric_id=12790,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")
