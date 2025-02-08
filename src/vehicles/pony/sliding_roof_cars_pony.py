from train import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # gen 5 start, only B and C lengths

    model_def = ModelDef(
        class_name="SlidingRoofCarConsist",
        base_numeric_id=24270,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="2_axle_1cc_filled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="SlidingRoofCarConsist",
        base_numeric_id=24280,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="4_axle_1cc_filled_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="SlidingRoofCarConsist",
        base_numeric_id=1000,
        gen=5,
        subtype="D",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar",
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        spriterow_num=0,
    )

    model_def.add_unit(
        class_name="FreightCar",
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        force_spriterow_group_in_output_spritesheet=1,  # special case
    )

    result.append(model_def)

    return result
