from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="MineralCoveredHopperCarSaltSwingRoof",
        base_numeric_id=27260,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="2_axle_1cc_filled_hoppers_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="MineralCoveredHopperCarSaltSwingRoof",
        base_numeric_id=22060,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="4_axle_1cc_filled_hoppers_32px"
    )

    result.append(model_def)

    return result
