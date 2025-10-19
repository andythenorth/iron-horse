from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="intrepid",
        base_numeric_id=21520,
        name="Intrepid",
        subrole="heavy_express",
        subrole_child_branch_num=-1,  # -ve because Joker
        power_by_power_source={
            "DIESEL": 2200,
        },
        random_reverse=True,
        gen=4,
        fixed_run_cost_points=40,  # give a bonus so this can be a genuine mixed-traffic engine
        intro_year_offset=6,  # let's be later for this one
        extended_vehicle_life=True,
        # add triple grey railfreight
        liveries=["BANGER_BLUE", "SUPERGRAPHIC", "RAILFREIGHT_RED_STRIPE"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=100,  # bonus over Wyvern, less than IRL as HP is nerfed
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """These are a bit duff, but they're a bit lighter than a Wyvern so we'll give em a go."""
    )
    model_def.define_foamer_facts(
        """BR Class 47, prime mover downrated for reliability"""
    )

    result.append(model_def)

    return result
