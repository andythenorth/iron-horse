from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="resilient",
        base_numeric_id=21000,
        name="Resilient",
        subrole="heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 2750,
        },
        random_reverse=True,
        gen=5,
        intro_year_offset=4,  # let's not have everything turn up in 1990
        fixed_run_cost_points=65,  # give a bonus so this can be a genuine mixed-traffic engine
        # add RfD Euro style triple grey?
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[
            "INTERCITY_RASPBERRY_RIPPLE",
            "RES",
            "FREIGHTLINER_GBRF",
            "DUTCH_1986",
            "DB_SCHENKER",
            "BANGER_BLUE",
        ],
        default_livery_extra_docs_examples=[
            ("COLOUR_BLUE", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
        sprites_additional_liveries_potential=True,  # add RfD Euro style triple grey?, Banger blue, but with black windows
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=103,
        vehicle_length=8,
        effect_offsets=[(2, 0)],
        spriterow_num=0,
    )

    model_def.define_description("""I've completely rebuilt some Intrepids.""")
    model_def.define_foamer_facts(
        """BR Class 47, Brush Class 57, original TTD UU '47'"""
    )

    result.append(model_def)

    return result
