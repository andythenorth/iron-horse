from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="grillage",
        base_numeric_id=30890,
        name="Grillage",
        subrole="super_heavy_freight",
        subrole_child_branch_num=-3,
        power_by_power_source={
            "DIESEL": 3500,
        },
        speed=87,  # these don't *have* to be replaced at game end
        random_reverse=True,
        gen=4,
        intro_year_offset=12,  # let's be later for this one
        liveries=[
            "STOCK_STANDARD",
            "SHOW_PONY",
            "BANGER_BLUE",
            "RAILFREIGHT_RED_STRIPE",
            "SUPERGRAPHIC",
        ],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="DieselEngineUnit",
        weight=128,
        vehicle_length=8,
        effect_offsets=[(0, 1), (0, -1)],  # double the smoke eh?
    )

    model_def.define_description("""""")
    model_def.define_foamer_facts(
        """Proposed BR high-horsepower freight locomotives of the 1960s and 1970s"""
    )

    result.append(model_def)

    return result
