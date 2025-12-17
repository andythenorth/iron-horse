from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="girt_licker",
        base_numeric_id=70,
        name="0-10-0 Girt Licker",
        subrole="super_heavy_freight",
        subrole_child_branch_num=-1,  # child branch 1 empty, for tech tree drawing reasons (blackthorn and quietus in branch -1)
        power_by_power_source={
            "STEAM": 1850,  # match to Vigilant
        },
        tractive_effort_coefficient=0.33,
        fixed_run_cost_points=250,  # cost malus, early heavy freight engines are too cheap to run relative to smaller engines
        gen=2,
        intro_year_offset=6,  # introduce a bit later
        liveries=["WORKHORSE", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="SteamEnginePoweredUnit",
        weight=100,
        vehicle_length=6,
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        unit_cls_name="SteamEngineTenderUnit",
        weight=45,
        vehicle_length=4,
        rel_spriterow_index=1,
    )

    model_def.define_description("""Big ugly thing. Power in spades though.""")
    model_def.define_foamer_facts("""Midland Railway 2290 'Big Bertha' Lickey Banker""")

    result.append(model_def)

    return result
