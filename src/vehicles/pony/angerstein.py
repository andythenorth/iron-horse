from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        id="angerstein",
        base_numeric_id=24790,
        name="Angerstein",
        subrole="metro",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "METRO": 1250,
        },
        random_reverse=True,
        gen=3,
        intro_year_offset=1,  # introduce later than gen epoch by design
        fixed_run_cost_points=120,  # substantial cost bonus for balance against same-era steam engines
        extended_vehicle_life=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="MetroUnit",
        weight=60,
        vehicle_length=8,
        spriterow_num=0,
    )

    model_def.define_description("""Are we going back to Romford?""")
    # https://www.checkerboardhill.com/2020/01/mtr-zer4-battery-electric-locomotives/
    model_def.define_foamer_facts(
        """CRRC ZER4 battery-electric locos for MTR (Hong Kong metro)"""
    )

    result.append(model_def)

    return result
