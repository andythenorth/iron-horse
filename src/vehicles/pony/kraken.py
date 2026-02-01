from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="PassengerEngineExpressRailcar",
        model_id="kraken",
        base_numeric_id=4900,
        name="Kraken",
        subrole="express_pax_railcar",
        subrole_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={
            "DIESEL": 840,
        },
        gen=3,
        intro_year_offset=2,  # introduce later by design
        # this railcar type specifies liveries per model_def for flexibility
        livery_group_name="gen_3_pax_express_railcar_liveries",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="DieselExpressRailcarPaxUnit",
        weight=50,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
        suppress_roof_sprite=True,
        repeat=2,
    )

    model_def.define_description("""The tide turns. Release the Kraken.""")
    model_def.define_foamer_facts("""GWR twin railcars""")

    result.append(model_def)

    return result
