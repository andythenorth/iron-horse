from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="mulberry",
        base_numeric_id=24430,
        name="Mulberry",
        subrole="metro_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "METRO": 1200,
        },
        random_reverse=True,
        base_track_type="METRO",
        gen=3,
        fixed_run_cost_points=120,  # substantial cost bonus for balance against same-era steam engines
        extended_vehicle_life=True,
        liveries=["METROLAND", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="MetroUnit", weight=48, vehicle_length=8, rel_spriterow_index=0
    )

    model_def.define_description("""Born slippy? Mega mega mega.""")
    model_def.define_foamer_facts("""London Underground battery-electric locos""")

    result.append(model_def)

    return result
