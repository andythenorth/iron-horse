from train import ExpressCarConsist, ExpressCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------

    # no NG express cars in pony, use mail car

    # --------------- pony ----------------------------------------------------------------------

    consist = ExpressCarConsist(
        roster_id="pony",
        base_numeric_id=17900,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="3_axle_solid_express_16px")

    consist = ExpressCarConsist(
        roster_id="pony",
        base_numeric_id=18100,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="3_axle_solid_express_16px")

    consist = ExpressCarConsist(
        roster_id="pony",
        base_numeric_id=10140,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="4_axle_solid_express_24px")

    consist = ExpressCarConsist(
        roster_id="pony",
        base_numeric_id=17920,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="3_axle_solid_express_16px")

    consist = ExpressCarConsist(
        roster_id="pony",
        base_numeric_id=18120,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="4_axle_solid_express_24px")

    consist = ExpressCarConsist(
        roster_id="pony",
        base_numeric_id=10430,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="2_axle_solid_express_16px")

    consist = ExpressCarConsist(
        roster_id="pony",
        base_numeric_id=17940,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="4_axle_solid_express_24px")

    consist = ExpressCarConsist(
        roster_id="pony",
        base_numeric_id=12260,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="4_axle_solid_express_32px")

    # !! should there be no 4/8 car for gen 5-6? (but add 8/8 car instead starting gen 4)

    consist = ExpressCarConsist(
        roster_id="pony",
        base_numeric_id=10450,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="2_axle_solid_express_16px")

    consist = ExpressCarConsist(
        roster_id="pony",
        base_numeric_id=18020,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="4_axle_solid_express_24px")

    consist = ExpressCarConsist(
        roster_id="pony",
        base_numeric_id=18040,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="4_axle_solid_express_32px")

    # no gen 6A 4/8 express car, removed Feb 2019, excessive number of express cars

    consist = ExpressCarConsist(
        roster_id="pony",
        base_numeric_id=18140,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="4_axle_solid_express_24px")

    consist = ExpressCarConsist(
        roster_id="pony",
        base_numeric_id=18000,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressCar, chassis="4_axle_solid_express_32px")
