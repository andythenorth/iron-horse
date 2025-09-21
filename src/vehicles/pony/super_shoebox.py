from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="super_shoebox",
        base_numeric_id=9920,
        name="Super Shoebox",
        subrole="heavy_express",
        subrole_child_branch_num=-3,
        power_by_power_source={"DIESEL": 1250, "OHLE": 2600},
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=6,
        # additional_liveries=["RAILFREIGHT_TRIPLE_GREY", "DUTCH"],
        additional_liveries=[
            "INTERCITY_RASPBERRY_RIPPLE",
            "RES",
            "SWOOSH",
            "DB_SCHENKER",
        ],  # "RAILFREIGHT_TRIPLE_GREY"
        decor_spriterow_num=6,
        show_decor_in_purchase_for_variants=[1],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectroDieselEngineUnit",
        weight=82,
        vehicle_length=8,
        effect_offsets=[(2, 0)],
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """It's a bigger Shoebox. Well not bigger. But more power in it. Right new paint too."""
    )
    model_def.define_foamer_facts("""BR Class 73, Class 71/74, proposed Class 75""")

    result.append(model_def)

    return result
