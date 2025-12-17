from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="debden",
        base_numeric_id=24440,
        name="Debden",
        subrole="metro_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "METRO": 600,
        },
        random_reverse=True,
        base_track_type="METRO",
        gen=1,
        fixed_run_cost_points=120,  # substantial cost bonus for balance against same-era steam engines
        extended_vehicle_life=True,
        liveries=["METROLAND", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="MetroUnit", weight=46, vehicle_length=8, rel_spriterow_index=0
    )

    model_def.define_description("""Is this London calling to the underworld?""")
    model_def.define_foamer_facts(
        """London Underground L11 battery-electric locomotive"""
    )

    result.append(model_def)

    return result
