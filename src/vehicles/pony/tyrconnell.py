from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="tyrconnell",
        base_numeric_id=930,
        name="4-8-0 Tyrconnell",
        subrole="universal",
        subrole_child_branch_num=-3,
        base_track_type="NG",
        power_by_power_source={
            "STEAM": 900,
        },
        tractive_effort_coefficient=0.28,
        gen=2,
        intro_year_offset=-5,  # introduce early eh
        random_reverse=False,
        liveries=["CLASSIC_LINES"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="SteamEnginePoweredUnit",
        weight=45,
        vehicle_length=5,
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        unit_cls_name="SteamEngineTenderUnit",
        weight=19,
        vehicle_length=3,
        rel_spriterow_index=1,
    )

    model_def.define_description("""A titan from the North. Steadfast and stout.""")
    model_def.define_foamer_facts(
        """Londonderry and Lough Swilly Railway Company 4-8-0 locomotives"""
    )

    result.append(model_def)

    return result
