from train import PanoramicCarConsist, PaxCar


def main(roster_id, **kwargs):
    # --------------- narrow gauge -----------------------------------------------------------------
    consist = PanoramicCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35130,
        gen=4,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, suppress_roof_sprite=True, chassis="4_axle_ng_24px")

    consist = PanoramicCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35140,
        gen=4,
        subtype="C",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, suppress_roof_sprite=True, chassis="4_axle_ng_32px")
