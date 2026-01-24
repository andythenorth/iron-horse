from train.model_def import ModelDef

def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="FreightEngineCargoSprinterMiddleEngine",
        model_id="brash_middle",
        cab_id="brash_cab",
        base_numeric_id=17050,
        name="Brash Powered Trailer",
        subrole="freight_railcar",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 0,
        },
        receives_easter_egg_haulage_speed_bonus=True,
        gen=5,
        intro_year_offset=3,  # introduce later than gen epoch by design
        liveries=["BANGER_BLUE", "LOWER_LINES", "VAPID_VOYAGER", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="DieselRailcarFreightUnit",
        weight=32,
        rel_spriterow_index=0,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_4",
    )

    model_def.define_description("""Runs like the wind.""")
    model_def.define_foamer_facts("""Windhoff MPV / CargoSprinter""")

    result.append(model_def)

    return result
