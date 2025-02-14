from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineRailcarConsist",
        base_id="slammer",
        base_numeric_id=21080,
        name="Slammer",
        subrole="pax_railcar",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 300,
        },
        gen=4,
        # introduce early by design
        intro_year_offset=-5,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselRailcarPaxUnit",
        weight=37,
        chassis="railcar_32px",
        tail_light="railcar_32px_2",
    )

    model_def.define_description(
        """Fast quiet trains for a new era. No more lurching Deasils."""
    )
    model_def.define_foamer_facts("""BR Class 108/117/121 and similar units""")

    result.append(model_def)

    return result
