from train import AutomobileLowFloorCarConsist, AutomobileCarAsymmetric


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------
    # intro gen 4

    consist = AutomobileLowFloorCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=26720,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(
        type=AutomobileCarAsymmetric, chassis="2_axle_lwb_filled_24px"
    )

    consist = AutomobileLowFloorCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=26730,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=AutomobileCarAsymmetric, chassis="4_axle_running_gear_only_32px"
    )

    consist = AutomobileLowFloorCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=26740,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(
        type=AutomobileCarAsymmetric, chassis="2_axle_lwb_filled_24px"
    )

    consist = AutomobileLowFloorCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=26750,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=AutomobileCarAsymmetric, chassis="4_axle_running_gear_only_32px"
    )
