from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_type_id="hurly_burly",
        base_numeric_id=21010,
        name="Hurly Burly",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "AC": 1800,
        },
        tractive_effort_coefficient=0.25,
        random_reverse=True,
        gen=2,
        pantograph_type="diamond-double",
        intro_year_offset=5,  # introduce later than gen epoch by design
        fixed_run_cost_points=180,  # substantial cost bonus for balance against same-era steam engines
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        default_livery_extra_docs_examples=[
            ("COLOUR_PINK", "COLOUR_WHITE"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_PINK"),
        ],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit", weight=99, vehicle_length=8, spriterow_num=0
    )

    model_def.define_description(
        """By eck, it's a big electric.  Better put some pennies in the meter."""
    )
    model_def.define_foamer_facts("""NER Class EE1""")

    result.append(model_def)

    return result
