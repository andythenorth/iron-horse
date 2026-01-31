from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="PassengerEngineRailcar",
        model_id="breeze",
        base_numeric_id=21850,
        name="Breeze",
        subrole="pax_railcar",
        subrole_child_branch_num=2,
        power_by_power_source={
            "OHLE": 520,
        },
        pantograph_type="z-shaped-single-with-base",
        receives_easter_egg_haulage_speed_bonus=True,
        gen=5,
        # introduce early by design
        intro_year_offset=-3,
        # this railcar type specifies liveries per model_def for flexibility
        livery_group_name="gen_5_electric_pax_railcar_liveries",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ElectricRailcarPaxUnit",
        weight=38,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
    )

    model_def.define_description("""So Swiftly Home""")
    model_def.define_foamer_facts("""BR Class 319, Class 455""")

    result.append(model_def)

    return result
