from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="grid",
        base_numeric_id=21620,
        name="Grid",
        subrole="super_heavy_freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 3450,
        },
        random_reverse=True,
        intro_year_offset=-8,  # let's be a little bit earlier for this one
        gen=5,
        liveries=[
            "SUPERGRAPHIC",
            "STOCK_STANDARD",
            "RAILFREIGHT_RED_STRIPE",
            "RAILFREIGHT_TRIPLE_GREY",
            "RAILFREIGHT_TRIPLE_GREY", # coal
            "SUPERGRAPHIC",
            "WORKHORSE",
        ],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="DieselEngineUnit",
        weight=120,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description("""These aren't bad at all.""")
    model_def.define_foamer_facts("""BR Class 56, GBRF Class 69""")

    result.append(model_def)

    return result
