from train import PanoramicCarConsist, PaxCar


def main(roster_id, **kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------
    consist_factory = PanoramicCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35130,
        gen=4,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="PaxCar", suppress_roof_sprite=True, chassis="4_axle_ng_24px"
    )

    result.append(consist_factory)

    consist_factory = PanoramicCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35140,
        gen=4,
        subtype="C",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="PaxCar", suppress_roof_sprite=True, chassis="4_axle_ng_32px"
    )

    result.append(consist_factory)

    return result
