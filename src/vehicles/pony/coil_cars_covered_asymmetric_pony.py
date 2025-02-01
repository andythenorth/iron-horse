from train import CoilCarCoveredAsymmetricConsist, CoilCarAsymmetric


def main(roster_id, **kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # start gen 4

    consist_factory = CoilCarCoveredAsymmetricConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23320,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=CoilCarAsymmetric, chassis="4_axle_filled_24px")

    result.append(consist_factory)

    consist_factory = CoilCarCoveredAsymmetricConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23330,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=CoilCarAsymmetric, chassis="4_axle_filled_32px")

    result.append(consist_factory)

    consist_factory = CoilCarCoveredAsymmetricConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23340,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=CoilCarAsymmetric, chassis="4_axle_1cc_filled_24px")

    result.append(consist_factory)

    consist_factory = CoilCarCoveredAsymmetricConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23350,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=CoilCarAsymmetric, chassis="4_axle_1cc_filled_32px")

    result.append(consist_factory)

    return result
