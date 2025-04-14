from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineRailcar",
        model_id="deasil",
        base_numeric_id=21240,
        name="Deasil",
        subrole="pax_railcar",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 200,
        },
        receives_easter_egg_haulage_speed_bonus=True,
        gen=3,
        # introduce early by design
        intro_year_offset=-5,
        # this railcar type specifies liveries per model_def for flexibility
        livery_group_name="default_pax_liveries",
        sprites_complete=True,
    )

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
