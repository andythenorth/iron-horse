from train import FlatCarTarpaulinConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    # gen 5 start, only B and C lengths

    consist = FlatCarTarpaulinConsist(
        roster_id="pony",
        base_numeric_id=9380,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_24px")

    consist = FlatCarTarpaulinConsist(
        roster_id="pony",
        base_numeric_id=16050,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")
