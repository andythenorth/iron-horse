from train.train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineRailcarConsist",
        base_id="tin_rocket",
        base_numeric_id=21160,
        name="Tin Rocket",
        subrole="pax_railcar",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 400,
        },
        gen=5,
        sprites_complete=True,
        # introduce early by design
        intro_year_offset=-5,
    )

    model_def.add_unit_def(
        class_name="DieselRailcarPaxUnit",
        weight=40,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
    )

    model_def.define_description(
        """Fast quiet trains for a new era. No more rattling Slammers."""
    )
    model_def.define_foamer_facts("""BR Class 153/155/156/158 <i>Sprinters</i>""")

    result.append(model_def)

    return result
