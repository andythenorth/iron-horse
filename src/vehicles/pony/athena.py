from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="PassengerEngineRailcar",
        model_id="athena",
        base_numeric_id=20030,
        name="Athena",
        subrole="pax_railcar",
        subrole_child_branch_num=2,
        power_by_power_source={
            "OHLE": 320,
        },
        pantograph_type="diamond-single-with-base",
        receives_easter_egg_haulage_speed_bonus=True,
        gen=3,
        # introduce early by design
        intro_year_offset=-3,
        # this railcar type specifies liveries per model_def for flexibility
        livery_group_name="gen_2_suburban_pax_liveries",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ElectricRailcarPaxUnit",
        weight=28,
        chassis="railcar_32px",
        tail_light="railcar_32px_1",
    )

    model_def.define_description("""World's Greatest Suburban Electric""")
    model_def.define_foamer_facts("""LNER <i>Tyneside Electrics</i>""")

    result.append(model_def)

    return result
