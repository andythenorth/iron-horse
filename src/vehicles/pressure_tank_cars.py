from train import GasTankCarPressureConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=15050,
        gen=2,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=15060,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=15070,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------
    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=9120,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=9220,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=9290,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=15230,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=15240,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=15250,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_32px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=15320,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_alt_16px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=15260,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_24px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=15270,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_32px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=15330,
        gen=6,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_alt_16px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=15280,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_24px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=15290,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_alt_32px")
