from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="cyclone",
        base_numeric_id=22130,
        name="Cyclone",
        subrole="express",
        subrole_child_branch_num=-3,
        power_by_power_source={
            "OHLE": 2200,
        },
        random_reverse=True,
        gen=5,
        pantograph_type="z-shaped-single",
        intro_year_offset=4,  # introduce later than gen epoch by design
        extended_vehicle_life=True,
        liveries=[
            "STOCK_STANDARD",
            "SHOW_PONY",
            "VAPID_VOYAGER",
            "LOWER_LINES",
            "INDUSTRIAL_YELLOW",
        ],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ElectricEngineUnit",
        weight=92,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """Nippy as a whippet, eats miles like hot dinners. Proper electric workhorse, that one."""
    )
    model_def.define_foamer_facts("""Austrian Federal Railways (ÖBB) 1163 class""")

    result.append(model_def)

    return result
