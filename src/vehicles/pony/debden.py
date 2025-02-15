from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        base_id="debden",
        base_numeric_id=24440,
        name="Debden",
        subrole="metro",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "METRO": 600,
        },
        random_reverse=True,
        base_track_type_name="METRO",
        gen=1,
        fixed_run_cost_points=120,  # substantial cost bonus for balance against same-era steam engines
        extended_vehicle_life=True,
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "INDUSTRIAL_YELLOW"],
        cabbage_new_livery_system=True,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="MetroUnit", weight=46, vehicle_length=8, spriterow_num=0
    )

    model_def.define_description("""Is this London calling to the underworld?""")
    model_def.define_foamer_facts(
        """London Underground L11 battery-electric locomotive"""
    )

    result.append(model_def)

    return result
