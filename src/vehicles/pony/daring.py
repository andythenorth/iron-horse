from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="daring",
        base_numeric_id=21710,
        name="Daring",
        subrole="express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 1750,
        },
        fixed_run_cost_points=116,  # give a small bonus so this can be a genuine mixed-traffic engine
        random_reverse=True,
        gen=4,
        intro_year_offset=1,  # let's be a littler later for this one
        default_livery_extra_docs_examples=[("COLOUR_GREEN", "COLOUR_WHITE")],
        caboose_family="gwr_1",
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "BANGER_BLUE"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=75,
        vehicle_length=8,
        effect_offsets=[(2, 0)],
        rel_spriterow_index=0,
    )

    model_def.define_description("""Fast and light, right good.""")
    model_def.define_foamer_facts("""BR Class 35 <i>Hymek</i>""")

    result.append(model_def)

    return result
