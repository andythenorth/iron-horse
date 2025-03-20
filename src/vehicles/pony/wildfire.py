from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="wildfire",
        base_numeric_id=39890,
        name="Wildfire",
        subrole="branch_express",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1650,
        },
        random_reverse=True,
        fixed_run_cost_points=100,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=5,  # not replaced by anything (?)
        intro_year_offset=7,  # introduce later than gen epoch by design
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "SWOOSH", "SWOOSH", "INDUSTRIAL_YELLOW"],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit", weight=72, vehicle_length=6, rel_spriterow_index=0
    )

    model_def.define_description(
        """"""
    )
    model_def.define_foamer_facts("""Vossloh G2000""")

    result.append(model_def)

    """

    model_def_clone = model_def.begin_clone(base_numeric_id=820, unit_repeats=[1])

    # this is a JFDI thing, the Lynx 2-unit version needs a reversed sprite, but the buy menu compositor does not support that as of Jan 2024, so hax
    model_def_clone.add_unit_def(
        class_name="DieselEngineUnit", weight=72, vehicle_length=6, rel_spriterow_index=1
    )

    # JFDI, the single unit should randomly reverse, the 2-unit version should not, so hax
    model_def_clone.random_reverse = False

    model_def = model_def_clone.complete_clone()

    result.append(model_def)
    """
    return result
