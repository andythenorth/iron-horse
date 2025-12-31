from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="PassengerEngineExpressRailcar",
        model_id="typhoon",
        base_numeric_id=5220,
        name="Typhoon",
        subrole="express_pax_railcar",
        subrole_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={
            "DIESEL": 1400,
        },
        gen=5,
        intro_year_offset=1,  # introduce later by design
        livery_group_name="gen_5_and_6_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="DieselExpressRailcarPaxUnit",
        weight=50,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    model_def.define_description("""Built to outrun the weather.""")
    model_def.define_foamer_facts("""BR Class 210 DEMU, NIR 450 Class DEMU""")

    result.append(model_def)

    return result
