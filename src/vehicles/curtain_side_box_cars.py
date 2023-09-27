from train import BoxCarCurtainSideConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------

    consist = BoxCarCurtainSideConsist(
        roster_id="pony",
        base_numeric_id=18650,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = BoxCarCurtainSideConsist(
        roster_id="pony",
        base_numeric_id=18670,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------

    consist = BoxCarCurtainSideConsist(
        roster_id="pony",
        base_numeric_id=18630,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = BoxCarCurtainSideConsist(
        roster_id="pony",
        base_numeric_id=18550,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_24px")

    consist = BoxCarCurtainSideConsist(
        roster_id="pony",
        base_numeric_id=18570,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    consist = BoxCarCurtainSideConsist(
        roster_id="pony",
        base_numeric_id=18590,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = BoxCarCurtainSideConsist(
        roster_id="pony",
        base_numeric_id=18610,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")
