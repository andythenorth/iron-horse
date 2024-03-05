from train import PassengerCarConsist, PaxCar


def main(roster_id, **kwargs):
    # --------------- narrow gauge -----------------------------------------------------------------
    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=35130,
        gen=4,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_24px")

    consist = PassengerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=35140,
        gen=4,
        subtype="C",
        base_track_type_name="NG",
        sprites_complete=False,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_ng_32px")
