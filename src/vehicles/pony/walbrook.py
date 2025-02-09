from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        id="walbrook",
        base_numeric_id=400,
        name="Walbrook",
        subrole="metro",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "METRO": 650,
        },
        gen=1,
        intro_year_offset=1,  # introduce later than gen epoch by design
        fixed_run_cost_points=120,  # substantial cost bonus for balance against same-era steam engines
        extended_vehicle_life=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="MetroUnit",
        weight=28,
        vehicle_length=4,
        spriterow_num=0,
        repeat=2,
    )

    model_def.define_description("""Are these glazed and dirty steps?""")
    model_def.define_foamer_facts("""District Railway electric locos""")

    result.append(model_def)

    return result
