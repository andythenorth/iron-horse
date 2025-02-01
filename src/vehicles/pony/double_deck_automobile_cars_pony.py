from train import AutomobileDoubleDeckCarConsist, AutomobileCarAsymmetric


def main(roster_id, **kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------    # intro gen 4

    consist_factory = AutomobileDoubleDeckCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=26760,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="AutomobileCarAsymmetric", chassis="2_axle_lwb_filled_24px"
    )

    result.append(consist_factory)

    consist_factory = AutomobileDoubleDeckCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30890,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="AutomobileCarAsymmetric", chassis="4_axle_running_gear_only_32px"
    )

    result.append(consist_factory)

    consist_factory = AutomobileDoubleDeckCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=26770,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="AutomobileCarAsymmetric", chassis="2_axle_lwb_filled_24px"
    )

    result.append(consist_factory)

    consist_factory = AutomobileDoubleDeckCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17330,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="AutomobileCarAsymmetric", chassis="4_axle_running_gear_only_32px"
    )
    """
    consist_factory = AutomobileDoubleDeckCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=5830,
        gen=5,
        subtype="D",
        sprites_complete=False,
    )

    consist_factory.add_unit(
        class_name="AutomobileCarAsymmetric",
        chassis="2_axle_running_gear_only_20px",
        spriterow_num=0,
    )

    consist_factory.add_unit(
        class_name="AutomobileCarAsymmetric",
        chassis="2_axle_running_gear_only_20px",
        spriterow_num=1,
    )
    """

    return result
