from train import FarmProductsBoxCarConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------
    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=1310,
        gen=1,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # no gen 2 for NG, straight to gen 3

    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=1360,
        gen=3,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=1520,
        gen=4,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # --------------- pony --------------------------------------------------------------------------
    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=2640,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=2630,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=2620,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_24px")

    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=2600,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=2610,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_24px")

    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=3570,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=2650,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=2660,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=1890,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_greebled_24px",
    )

    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=1900,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_filled_greebled_32px",
    )
