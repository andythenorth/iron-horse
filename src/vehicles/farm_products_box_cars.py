from train import FarmProductsBoxCarConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------
    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=10350,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # no gen 2 for NG, straight to gen 3

    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=10400,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=10560,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # --------------- pony --------------------------------------------------------------------------
    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=11680,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=12740,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_24px")

    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=11670,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=11660,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_24px")

    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=11640,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=11650,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_24px")

    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=12610,
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
        base_numeric_id=11690,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = FarmProductsBoxCarConsist(
        roster_id="pony",
        base_numeric_id=11700,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")
