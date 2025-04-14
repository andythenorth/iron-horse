from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="dynamo",
        base_numeric_id=20970,
        name="Dynamo",
        subrole="express",
        subrole_child_branch_num=-3,
        power_by_power_source={
            "AC": 1900,  # matches or better than equivalent gen steam engines
        },
        random_reverse=True,
        gen=3,
        pantograph_type="diamond-double",
        intro_year_offset=5,  # introduce later than gen epoch by design
        extended_vehicle_life=True,
        fixed_run_cost_points=180,  # substantial cost bonus for balance against same-era steam engines
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA"],
        default_livery_extra_docs_examples=[
            ("COLOUR_PINK", "COLOUR_WHITE"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_PINK"),
        ],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit",
        weight=92,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description("""Nowt to fuss about with this one.""")
    model_def.define_foamer_facts(
        """SR CC1/CC2 locomotives, English Electric Class EP01 exported from UK to Poland"""
    )

    result.append(model_def)

    return result
