from train import CoilCarCoveredAsymmetricConsist, CoilCarAsymmetric


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------
    # start gen 4

    consist = CoilCarCoveredAsymmetricConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=15800,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=CoilCarAsymmetric, chassis="4_axle_filled_24px")

    consist = CoilCarCoveredAsymmetricConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=13510,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=CoilCarAsymmetric, chassis="4_axle_filled_32px")

    consist = CoilCarCoveredAsymmetricConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=13430,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=CoilCarAsymmetric, chassis="4_axle_1cc_filled_24px")

    consist = CoilCarCoveredAsymmetricConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=15730,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=CoilCarAsymmetric, chassis="4_axle_1cc_filled_32px")
