from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="pinhorse",
        base_numeric_id=21860,
        name="Pinhorse",
        subrole="branch_express",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 1050,  # matched to Stoat
        },
        random_reverse=True,
        pantograph_type="diamond-single",
        gen=2,
        intro_year_offset=3,  # introduce later than gen epoch by design
        fixed_run_cost_points=120,  # substantial cost bonus for balance against same-era steam engines
        extended_vehicle_life=True,
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "BANGER_BLUE"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit", weight=60, vehicle_length=6, rel_spriterow_index=0
    )

    model_def.define_description(
        """These are bob on. For small jobs, you won't go far wrong with em."""
    )
    model_def.define_foamer_facts("""Metropolitan Railway electric locos""")

    result.append(model_def)

    return result
