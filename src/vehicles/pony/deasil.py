from train.train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineRailcarConsist",
        base_id="deasil",
        base_numeric_id=21240,
        name="Deasil",
        subrole="pax_railcar",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 200,
        },
        gen=3,
        sprites_complete=True,
        intro_year_offset=-5,
    )  # introduce early by design

    model_def.add_unit_def(
        class_name="DieselRailcarPaxUnit",
        weight=30,
        chassis="railcar_32px",
        tail_light="railcar_32px_1",
    )

    model_def.define_description(
        """Fast quiet trains for a new era. No more noisy steam engines."""
    )
    model_def.define_foamer_facts("""LNER / Armstrong-Whitworth Railcars""")

    result.append(model_def)

    return result
