from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="MailEngineRailcar",
        model_type_id="plastic_postbox",
        base_numeric_id=21420,
        name="Plastic Postbox",
        subrole="mail_railcar",
        subrole_child_branch_num=2,
        replacement_model_model_type_id="pylon",  # consolidates to electro-diesel with Pylon
        power_by_power_source={
            "DIESEL": 560,
        },
        gen=5,
        sprites_complete=True,
        intro_year_offset=-5,
    )  # introduce early by design

    model_def.add_unit_def(
        class_name="DieselRailcarMailUnit",
        weight=37,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
    )

    model_def.define_description(
        """The most modern way to move mail and other parcels."""
    )
    model_def.define_foamer_facts(
        """BR Class 128/130, BR Class 153/155/156/158 <i>Sprinters</i>"""
    )

    result.append(model_def)

    return result
