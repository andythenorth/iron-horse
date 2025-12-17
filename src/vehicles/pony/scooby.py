from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="MailEngineRailcar",
        model_id="scooby",
        base_numeric_id=21430,
        name="Scooby",
        subrole="mail_railcar",
        subrole_child_branch_num=2,
        power_by_power_source={
            "DIESEL": 420,
        },
        receives_easter_egg_haulage_speed_bonus=True,
        gen=4,
        # introduce early by design
        intro_year_offset=-5,
        livery_group_name="gen_4_diesel_railcar_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="DieselRailcarMailUnit",
        weight=37,
        chassis="railcar_32px",
        tail_light="railcar_32px_2",
    )

    model_def.define_description(
        """A more modern way to move mail and other parcels."""
    )
    model_def.define_foamer_facts("""BR Class 128/130""")

    result.append(model_def)

    return result
