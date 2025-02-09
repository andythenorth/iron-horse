from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="griffon",
        base_numeric_id=21360,
        name="Griffon",  # Griffon and Shredder names are wrong way round, but seems to suit the shapes so eh, leave it :)
        subrole="branch_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 1650,
        },
        random_reverse=True,
        fixed_run_cost_points=100,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=5,  # not replaced by anything (?)
        caboose_family="railfreight_2",
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[
            "RAILFREIGHT_TRIPLE_GREY",
            "RAILFREIGHT_TRIPLE_GREY_COAL",
            "DB_SCHENKER",
            "BANGER_BLUE",
        ],
        default_livery_extra_docs_examples=[
            ("COLOUR_GREY", "COLOUR_YELLOW"),
            ("COLOUR_WHITE", "COLOUR_GREY"),
            ("COLOUR_GREY", "COLOUR_GREY"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
        ],
        decor_spriterow_num=5,
        show_decor_in_purchase_for_variants=[0, 1, 2],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit", weight=74, vehicle_length=6, spriterow_num=0
    )

    model_def.define_description(
        """Kelpie were right good, this is the rebuilt version."""
    )
    model_def.define_foamer_facts("""BR Class 33""")

    result.append(model_def)

    model_def = model_def.begin_clone(base_numeric_id=800, unit_repeats=[2])

    model_def.complete_clone()

    result.append(model_def)

    return result
