from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="borax",
        base_numeric_id=24780,
        name="Borax",
        subrole="metro",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "METRO": 950,
        },
        random_reverse=True,
        base_track_type_name="METRO",
        gen=2,
        intro_year_offset=1,  # introduce later than gen epoch by design
        fixed_run_cost_points=120,  # substantial cost bonus for balance against same-era steam engines
        extended_vehicle_life=True,
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "INDUSTRIAL_YELLOW"],
        cabbage_new_livery_system=True,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="MetroUnit", weight=60, vehicle_length=8, rel_spriterow_index=0
    )

    model_def.define_description("""Is London drowning? Because I live by the river.""")
    model_def.define_foamer_facts("""Metropolitan Railway electric locos""")

    result.append(model_def)

    return result
