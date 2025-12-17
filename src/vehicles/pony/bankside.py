from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="MailEngineMetro",
        model_id="bankside",
        base_numeric_id=1920,
        name="Bankside",
        subrole="mail_metro",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "METRO": 1100,
        },
        base_track_type="METRO",
        gen=3,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="MetroUnit",
        weight=32,
        # set capacity for freight; mail will be automatically calculated
        capacity=30,
        chassis="metro_heavy_32px",
        tail_light="metro_32px_3",
        repeat=2,
    )

    model_def.define_description("""Is it the screech of brakes?""")
    model_def.define_foamer_facts("""London Underground S Stock""")

    result.append(model_def)

    return result
