from train import BoxCarVehiclePartsConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    # starts gen 4, B and C only

    consist = BoxCarVehiclePartsConsist(
        roster_id="pony",
        base_numeric_id=18300,
        gen=4,
        subtype="B",
        intro_year_offset=3,  # let's be a little bit later for this one
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_1cc_filled_24px")

    consist = BoxCarVehiclePartsConsist(
        roster_id="pony",
        base_numeric_id=13670,
        gen=4,
        subtype="C",
        intro_year_offset=3,  # let's be a little bit later for this one
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    consist = BoxCarVehiclePartsConsist(
        roster_id="pony",
        base_numeric_id=18320,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_1cc_filled_24px",
    )

    consist = BoxCarVehiclePartsConsist(
        roster_id="pony",
        base_numeric_id=13690,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )
