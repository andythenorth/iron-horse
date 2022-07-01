from train import FlatCarTarpaulinConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    # gen 5 start, only B and C lengths

    consist = FlatCarTarpaulinConsist(
        roster_id="pony", base_numeric_id=9380, gen=5, subtype="B", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_24px")

    consist = FlatCarTarpaulinConsist(
        roster_id="pony", base_numeric_id=9390, gen=5, subtype="C", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    consist = FlatCarTarpaulinConsist(
        roster_id="pony", base_numeric_id=9410, gen=6, subtype="B", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_24px")

    consist = FlatCarTarpaulinConsist(
        roster_id="pony", base_numeric_id=9440, gen=6, subtype="C", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")

    # --------------- ibex ----------------------------------------------------------------------

    # gen 5 start, only B and C lengths

    consist = FlatCarTarpaulinConsist(
        roster_id="ibex", base_numeric_id=8810, gen=5, subtype="B", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_24px")

    consist = FlatCarTarpaulinConsist(
        roster_id="ibex", base_numeric_id=8820, gen=5, subtype="C", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    consist = FlatCarTarpaulinConsist(
        roster_id="ibex", base_numeric_id=8830, gen=6, subtype="B", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_24px")

    consist = FlatCarTarpaulinConsist(
        roster_id="ibex", base_numeric_id=8840, gen=6, subtype="C", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")
