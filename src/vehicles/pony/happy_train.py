from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineRailcar",
        model_id="happy_train",
        base_numeric_id=20330,
        name="Happy Train",
        subrole="pax_railcar",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 500,
        },
        gen=6,
        # introduce early by design
        intro_year_offset=-5,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselRailcarPaxUnit",
        weight=40,
        chassis="railcar_32px",
        tail_light="railcar_32px_2",
    )

    model_def.define_description(
        """Fast quiet trains for a new era. No more life-expired Tin Rockets."""
    )
    model_def.define_foamer_facts("""Siemens <i>Desiro</i>""")

    result.append(model_def)

    return result
