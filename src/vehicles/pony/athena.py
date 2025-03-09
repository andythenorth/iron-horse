from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineRailcar",
        model_id="athena",
        base_numeric_id=20030,
        name="Athena",
        subrole="pax_railcar",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 320,
        },
        pantograph_type="diamond-single-with-base",
        easter_egg_haulage_speed_bonus=True,
        gen=3,
        # introduce early by design
        intro_year_offset=-3,
        # this railcar type specifies liveries per model_def for flexibility
        livery_group_name="suburban_pax_liveries",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricRailcarPaxUnit",
        weight=28,
        chassis="railcar_32px",
        tail_light="railcar_32px_1",
    )

    model_def.define_description("""World's Greatest Suburban Electric""")
    model_def.define_foamer_facts("""LNER <i>Tyneside Electrics</i>""")

    result.append(model_def)

    return result
