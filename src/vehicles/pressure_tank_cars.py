from train import GasTankCarPressureConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=6010,
        gen=2,
        subtype="U",
        base_track_type="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=6020,
        gen=3,
        subtype="U",
        base_track_type="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=6030,
        gen=4,
        subtype="U",
        base_track_type="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------
    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=6160,
        gen=2,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=6170,
        gen=3,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=6180,
        gen=3,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=6190,
        gen=4,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=6200,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=6210,
        gen=4,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_32px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=6280,
        gen=5,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=6220,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=6230,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_32px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=6290,
        gen=6,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=6240,
        gen=6,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = GasTankCarPressureConsist(
        roster_id="pony",
        base_numeric_id=6250,
        gen=6,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_32px")
