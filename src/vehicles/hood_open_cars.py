from train import OpenCarHoodConsist, FreightCar


def main():

    # --------------- pony ----------------------------------------------------------------------

    # only type A for gen 1

    consist = OpenCarHoodConsist(
        roster_id="pony",
        base_numeric_id=7480,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    # no type A for gen 2, gen 1 type A continues, also no gen 2 type B

    consist = OpenCarHoodConsist(
        roster_id="pony",
        base_numeric_id=7500,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = OpenCarHoodConsist(
        roster_id="pony",
        base_numeric_id=7510,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = OpenCarHoodConsist(
        roster_id="pony",
        base_numeric_id=7520,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = OpenCarHoodConsist(
        roster_id="pony",
        base_numeric_id=7530,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_24px")

    consist = OpenCarHoodConsist(
        roster_id="pony",
        base_numeric_id=7540,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = OpenCarHoodConsist(
        roster_id="pony",
        base_numeric_id=7550,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")

    consist = OpenCarHoodConsist(
        roster_id="pony",
        base_numeric_id=7560,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = OpenCarHoodConsist(
        roster_id="pony",
        base_numeric_id=7570,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")
