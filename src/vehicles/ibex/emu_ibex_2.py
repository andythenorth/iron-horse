from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="PassengerEngineRailcar",
        model_id="emu_ibex_2",
        base_numeric_id=28430,
        name="BLS Ce 2/4",
        subrole="pax_railcar",
        subrole_child_branch_num=2,
        power_by_power_source={
            "OHLE": 320,
        },
        pantograph_type="diamond-single-with-base",
        receives_easter_egg_haulage_speed_bonus=True,
        gen=2,
        # this railcar type specifies liveries per model_def for flexibility
        livery_group_name="default_suburban_pax_liveries",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="ElectricRailcarPaxUnit",
        weight=28,
        chassis="railcar_32px",
        tail_light="railcar_32px_1",
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts("""BLS Ce 2/4""")

    result.append(model_def)

    return result
