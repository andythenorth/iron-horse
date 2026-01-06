from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="resilient",
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
        liveries=[
            "RIDEWELL",
            "FRUIT_RIPPLE",
            "MAIL_BY_RAIL",
            "FREIGHTLINER_GBRF",
            "CONVENTIONAL_WISDOM",
            "LOWER_LINES",
            "BANGER_BLUE",
        ],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="DieselEngineUnit",
        weight=103,
        vehicle_length=8,
        effect_offsets=[(2, 0)],
        rel_spriterow_index=0,
    )

    model_def.define_description("""I've completely rebuilt some Intrepids.""")
    model_def.define_foamer_facts(
        """BR Class 47, Brush Class 57, original TTD UU '47'"""
    )

    result.append(model_def)

    return result
