from train import OpenCarHoodConsist, FreightCar


def main(roster_id):
    # --------------- standard gauge ---------------------------------------------------------------
    # only type A for gen 1

    consist = OpenCarHoodConsist(
        roster_id=roster_id,
        base_numeric_id=16520,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    # no type A for gen 2, gen 1 type A continues, also no gen 2 type B

    consist = OpenCarHoodConsist(
        roster_id=roster_id,
        base_numeric_id=16540,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = OpenCarHoodConsist(
        roster_id=roster_id,
        base_numeric_id=16550,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = OpenCarHoodConsist(
        roster_id=roster_id,
        base_numeric_id=16560,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = OpenCarHoodConsist(
        roster_id=roster_id,
        base_numeric_id=16570,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_24px")

    consist = OpenCarHoodConsist(
        roster_id=roster_id,
        base_numeric_id=16580,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = OpenCarHoodConsist(
        roster_id=roster_id,
        base_numeric_id=16590,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")
