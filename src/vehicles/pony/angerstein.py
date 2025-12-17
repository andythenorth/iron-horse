from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="angerstein",
        base_numeric_id=24790,
        name="Angerstein",
        subrole="metro_freight",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "METRO": 1250,
        },
        random_reverse=True,
        base_track_type="METRO",
        gen=3,
        intro_year_offset=1,  # introduce later than gen epoch by design
        fixed_run_cost_points=120,  # substantial cost bonus for balance against same-era steam engines
        extended_vehicle_life=True,
        liveries=["METROLAND", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="MetroUnit",
        weight=60,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description("""Are we going back to Romford?""")
    # https://www.checkerboardhill.com/2020/01/mtr-zer4-battery-electric-locomotives/
    model_def.define_foamer_facts(
        """CRRC ZER4 battery-electric locos for MTR (Hong Kong metro)"""
    )

    result.append(model_def)

    return result
