from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="phoenix",
        base_numeric_id=21120,
        name="Phoenix",
        subrole="express",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 2200,
        },
        fixed_run_cost_points=42,  # give a huge bonus so this can be a genuine mixed-traffic engine
        random_reverse=True,
        gen=5,
        # red stripe? Teeside steelmaster?
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=[
            "VANILLA",
            "RAILFREIGHT_TRIPLE_GREY",
            "RAILFREIGHT_TRIPLE_GREY_COAL",
            "SWOOSH",
            "DB_SCHENKER",
            "LOADHAUL",
            "SWOOSH",
            "BANGER_BLUE",
        ],
        default_livery_extra_docs_examples=[("COLOUR_DARK_BLUE", "COLOUR_WHITE")],
        cabbage_new_livery_system=True,
        caboose_family="railfreight_2",
        decor_spriterow_num=8,
        show_decor_in_purchase_for_variants=[2, 3],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit", weight=110, vehicle_length=8, rel_spriterow_index=0
    )

    model_def.define_description(
        """We made these by uprating the Growler engine.  New paint too, don't spoil it."""
    )
    model_def.define_foamer_facts(
        """refurbished BR Class 37, with new alternator and uprated engine (per 2,000hp 37292)"""
    )

    result.append(model_def)

    return result
