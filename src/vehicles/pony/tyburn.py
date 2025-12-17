from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="MailEngineMetro",
        model_id="tyburn",
        base_numeric_id=2190,
        name="Tyburn",
        subrole="mail_metro",
        subrole_child_branch_num=1,
        power_by_power_source={
            "METRO": 850,
        },
        base_track_type="METRO",
        gen=2,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="MetroUnit",
        weight=29,
        # set capacity for freight; mail will be automatically calculated
        capacity=27,
        chassis="metro_low_floor_32px",
        tail_light="metro_32px_2",
        repeat=2,
    )

    model_def.define_description(
        """Do moles live in holes underground? Can they be found?"""
    )
    model_def.define_foamer_facts("""London Underground 1938/1949 Stock""")

    result.append(model_def)

    return result
