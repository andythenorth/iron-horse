from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineRailcar",
        model_id="breeze",
        base_numeric_id=21850,
        name="Breeze",
        subrole="pax_railcar",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 520,
        },
        pantograph_type="z-shaped-single-with-base",
        easter_egg_haulage_speed_bonus=True,
        gen=5,
        sprites_complete=True,
        intro_year_offset=-3,  # introduce early by design
    )

    model_def.add_unit_def(
        class_name="ElectricRailcarPaxUnit",
        weight=38,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
    )

    model_def.define_description("""So Swiftly Home""")
    model_def.define_foamer_facts("""BR Class 319, Class 455""")

    result.append(model_def)

    return result
