from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="smizzle",
        base_numeric_id=21580,
        name="Smizzle",
        subrole="freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1750,
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=-1,  # introduce earlier by design
        liveries=[
            "CLASSIC_LINES",
            "WORKHORSE",
            "STOCK_STANDARD",
            "RAILFREIGHT_RED_STRIPE",
            "INDUSTRIAL_YELLOW",
        ],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="DieselEngineUnit",
        weight=97,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description("""""")
    model_def.define_foamer_facts(
        """English Electric locomotives for Queensland and Western Australia, Baldwin DRS-6-4-660NA"""
    )

    result.append(model_def)

    return result
