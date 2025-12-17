from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="PassengerEngineRailcar",
        model_id="zeus",
        base_numeric_id=22240,
        name="Zeus",
        subrole="pax_railcar",
        subrole_child_branch_num=2,
        power_by_power_source={
            "OHLE": 620,
        },
        pantograph_type="z-shaped-single-with-base",
        receives_easter_egg_haulage_speed_bonus=True,
        gen=6,
        # introduce early by design
        intro_year_offset=-3,
        # this railcar type specifies liveries per model_def for flexibility
        livery_group_name="gen_6_suburban_pax_liveries",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ElectricRailcarPaxUnit",
        weight=39,
        chassis="railcar_32px",
        tail_light="railcar_32px_2",
    )

    model_def.define_description("""Gets you from A to Z and back.""")
    model_def.define_foamer_facts("""BR Class 365 <i>Networker Express</i>""")

    result.append(model_def)

    return result
