from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_type_id="cyclone",
        base_numeric_id=27870,
        name="Cyclone",
        subrole="express",
        subrole_child_branch_num=-3,
        power_by_power_source={
            "AC": 2200,
        },
        random_reverse=True,
        gen=5,
        pantograph_type="z-shaped-single",
        intro_year_offset=4,  # introduce later than gen epoch by design
        extended_vehicle_life=True,
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "SWOOSH", "SWOOSH", "DB_SCHENKER", "INDUSTRIAL_YELLOW"],
        default_livery_extra_docs_examples=[
            ("COLOUR_PINK", "COLOUR_WHITE"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_YELLOW"),
        ],
        cabbage_new_livery_system=True,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit", weight=92, vehicle_length=8, spriterow_num=0
    )

    model_def.define_description(
        """Nippy as a whippet, eats miles like hot dinners. Proper electric workhorse, that one."""
    )
    model_def.define_foamer_facts("""Austrian Federal Railways (ÖBB) 1163 class""")

    result.append(model_def)

    return result
