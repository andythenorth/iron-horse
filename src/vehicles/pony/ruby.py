from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="MailEngineRailcarConsist",
        base_id="ruby",
        base_numeric_id=28310,
        name="Ruby",
        subrole="mail_railcar",
        subrole_child_branch_num=1,
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 600,
        },
        gen=4,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselRailcarMailUnit",
        weight=20,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_24px",
        tail_light="railcar_24px_1",
    )

    model_def.define_description(
        """A modern way to move mail and other packages. I must regret, we have not yet accommodated goats."""
    )
    model_def.define_foamer_facts("""CFC Autorail Billard, CFC X2000/X5000""")

    result.append(model_def)

    return result
