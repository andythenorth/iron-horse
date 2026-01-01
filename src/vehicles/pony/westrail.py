from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="westrail",
        base_numeric_id=23000,
        name="Westrail",
        subrole="freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 2200,
            "OHLE": 3450,
        },
        pantograph_type="z-shaped-single",
        # no random reverse
        gen=5,
        intro_year_offset=6,  # introduce later than gen epoch by design
        liveries=[
            "INVERSIONS",
            "STOCK_STANDARD",
            "STOCK_STANDARD",
            "LOWER_LINES",
            "INDUSTRIAL_YELLOW",
        ],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ElectroDieselEngineUnit",
        weight=98,
        vehicle_length=8,
        effect_offsets=[(2, 0)],
        rel_spriterow_index=0,
    )

    model_def.define_description("""Looks tidy, works anywhere.""")
    model_def.define_foamer_facts(
        """Westrail P Class (Australia), Spoornet Class 38-000 (South Africa); bo-bo-bo wheel arrangement"""
    )

    result.append(model_def)

    return result
