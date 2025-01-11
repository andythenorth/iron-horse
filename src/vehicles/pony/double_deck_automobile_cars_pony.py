from train import AutomobileDoubleDeckCarConsist, AutomobileCarAsymmetric


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------    # intro gen 4

    consist = AutomobileDoubleDeckCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=26760,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCarAsymmetric, chassis="2_axle_lwb_filled_24px")

    consist = AutomobileDoubleDeckCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30890,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=AutomobileCarAsymmetric, chassis="4_axle_running_gear_only_32px"
    )

    consist = AutomobileDoubleDeckCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=26770,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCarAsymmetric, chassis="2_axle_lwb_filled_24px")

    consist = AutomobileDoubleDeckCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17330,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=AutomobileCarAsymmetric, chassis="4_axle_running_gear_only_32px"
    )
    """
    consist = AutomobileDoubleDeckCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=5830,
        gen=5,
        subtype="D",
        sprites_complete=False,
    )

    consist.add_unit(
        type=AutomobileCarAsymmetric,
        chassis="2_axle_running_gear_only_20px",
        spriterow_num=0,
    )

    consist.add_unit(
        type=AutomobileCarAsymmetric,
        chassis="2_axle_running_gear_only_20px",
        spriterow_num=1,
    )
    """
