from train import TankCarSulphurConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------
    consist = TankCarSulphurConsist(
        roster_id="pony",
        base_numeric_id=12810,
        gen=2,
        subtype="A",
        base_track_type_name="NG",
        intro_year_offset=-10,  # let's be earlier for this one
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = TankCarSulphurConsist(
        roster_id="pony",
        base_numeric_id=12830,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    """ # restore in next version
    consist = TankCarSulphurConsist(
        roster_id="pony",
        base_numeric_id=17570,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")
    """
    # --------------- pony ----------------------------------------------------------------------
    consist = TankCarSulphurConsist(
        roster_id="pony",
        base_numeric_id=16080,
        gen=2,
        subtype="A",
        intro_year_offset=-10,  # let's be earlier for this one
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = TankCarSulphurConsist(
        roster_id="pony",
        base_numeric_id=9660,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="3_axle_filled_16px")

    consist = TankCarSulphurConsist(
        roster_id="pony",
        base_numeric_id=9680,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = TankCarSulphurConsist(
        roster_id="pony",
        base_numeric_id=19270,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = TankCarSulphurConsist(
        roster_id="pony",
        base_numeric_id=19290,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_24px")

    consist = TankCarSulphurConsist(
        roster_id="pony",
        base_numeric_id=19310,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_32px")

    consist = TankCarSulphurConsist(
        roster_id="pony",
        base_numeric_id=19330,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_alt_16px")

    consist = TankCarSulphurConsist(
        roster_id="pony",
        base_numeric_id=19350,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_24px")

    consist = TankCarSulphurConsist(
        roster_id="pony",
        base_numeric_id=19370,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_32px")
