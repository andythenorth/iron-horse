from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="PassengerEngineExpressRailcar",
        model_id="high_flyer",
        base_numeric_id=15310,
        name="High Flyer",
        subrole="express_pax_railcar",
        subrole_child_branch_num=-2,  # joker to hide them from simplified mode
        power_by_power_source={
            "OHLE": 1600,
        },
        pantograph_type="diamond-single-with-base",
        gen=3,
        intro_year_offset=2,  # introduce later by design
        # this railcar type specifies liveries per model_def for flexibility
        livery_group_name="default_suburban_pax_liveries",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ElectricExpressRailcarPaxUnit",
        weight=48,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    model_def.define_description("""All Pullman Electric Express.""")
    model_def.define_foamer_facts("""SR 5-BEL <i>Brighton Belle</i>""")

    result.append(model_def)

    return result
