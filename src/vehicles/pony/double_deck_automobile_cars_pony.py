from train import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------    # intro gen 4

    model_def = ModelDef(
        class_name="AutomobileDoubleDeckCarConsist",
        base_numeric_id=26760,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="AutomobileCarAsymmetric", chassis="2_axle_lwb_filled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="AutomobileDoubleDeckCarConsist",
        base_numeric_id=30890,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="AutomobileCarAsymmetric", chassis="4_axle_running_gear_only_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="AutomobileDoubleDeckCarConsist",
        base_numeric_id=26770,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="AutomobileCarAsymmetric", chassis="2_axle_lwb_filled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="AutomobileDoubleDeckCarConsist",
        base_numeric_id=17330,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="AutomobileCarAsymmetric", chassis="4_axle_running_gear_only_32px"
    )

    result.append(model_def)
    """

    model_def =ModelDef(
        class_name="AutomobileDoubleDeckCarConsist",
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=5830,
        gen=5,
        subtype="D",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="AutomobileCarAsymmetric",
        chassis="2_axle_running_gear_only_20px",
        spriterow_num=0,
    )

    model_def.add_unit_def(
        class_name="AutomobileCarAsymmetric",
        chassis="2_axle_running_gear_only_20px",
        spriterow_num=1,
    )

    result.append(model_def)
    """

    return result
