from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_type_id="ultra_shoebox",
        base_numeric_id=21340,
        name="Ultra Shoebox",
        subrole="heavy_express",
        subrole_child_branch_num=-3,
        power_by_power_source={"DIESEL": 1650, "AC": 2800},
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=5,
        intro_year_offset=6,  # earlier than anything IRL, but we want 125 mph capability so eh, there we go
        extended_vehicle_life=True,  # because long time until replaced
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "SWOOSH", "DB_SCHENKER", "BANGER_BLUE"],
        default_livery_extra_docs_examples=[
            ("COLOUR_RED", "COLOUR_RED"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
            ("COLOUR_PURPLE", "COLOUR_WHITE"),
            ("COLOUR_CREAM", "COLOUR_MAUVE"),
            ("COLOUR_YELLOW", "COLOUR_YELLOW"),
            ("COLOUR_DARK_BLUE", "COLOUR_BLUE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
        ],
        cabbage_new_livery_system=True,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectroDieselEngineUnit",
        weight=84,
        vehicle_length=8,
        effect_offsets=[(2, 0)],
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """Top to bottom, it's an old Shoebox made new. Right powerful small engines."""
    )
    model_def.define_foamer_facts(
        """Network Rail / GBRF Class 73/9 (re-engineered), BR Class 74, proposed Class 75"""
    )

    result.append(model_def)

    return result
