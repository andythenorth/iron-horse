from train.factory import ModelDef

# implemented as dual headed, it really is just the nicer way to build these units (esp. when adding container wagons)

# NOTE that cargo sprinter will NOT randomise containers on load as of Dec 2020 - there is a bug with rear unit running unwanted triggers and re-randomising in depots etc


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="MailEngineCargoSprinterEngineConsist",
        base_id="cargo_sprinter",
        base_numeric_id=25840,
        name="Cargo Sprinter",
        subrole="mail_railcar",  # abuse of existing railcar role for convenience
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1650,  # matched to Griffon, Ultra Shoebox
        },
        gen=6,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselRailcarMailUnit",
        weight=32,
        spriterow_num=0,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_4",
    )

    model_def.define_description("""Runs like the wind.""")
    model_def.define_foamer_facts("""Windhoff MPV""")

    result.append(model_def)

    return result
