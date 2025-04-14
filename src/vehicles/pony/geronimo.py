from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineRailcar",
        model_id="geronimo",
        base_numeric_id=20020,
        name="Geronimo",
        subrole="pax_railcar",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 420,  # RL EMU HP is much lower per single car, but eh
        },
        pantograph_type="z-shaped-single-with-base",
        receives_easter_egg_haulage_speed_bonus=True,
        gen=4,
        # introduce early by design
        intro_year_offset=-3,
        # this railcar type specifies liveries per model_def for flexibility
        livery_group_name="suburban_pax_liveries",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricRailcarPaxUnit",
        weight=35,
        chassis="railcar_32px",
        tail_light="railcar_32px_2",
    )

    model_def.define_description("""More Speed. More Comfort. More Trains.""")
    model_def.define_foamer_facts("""BR 2-HAP, 4EPB, Class 302""")

    result.append(model_def)

    return result
