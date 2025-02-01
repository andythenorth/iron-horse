from train import ConsistFactory


def main(roster_id, **kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="MineralCoveredHopperCarSaltSwingRoofConsist",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=27260,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar", chassis="2_axle_1cc_filled_hoppers_24px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="MineralCoveredHopperCarSaltSwingRoofConsist",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=22060,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar", chassis="4_axle_1cc_filled_hoppers_32px"
    )

    result.append(consist_factory)

    return result
