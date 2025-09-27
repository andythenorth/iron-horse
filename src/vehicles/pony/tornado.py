from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="tornado",
        base_numeric_id=21750,
        name="Tornado",
        subrole="branch_express",
        subrole_child_branch_num=2,
        power_by_power_source={"DIESEL": 750, "OHLE": 1900},
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=5,
        intro_year_offset=6,  # introduce later than gen epoch by design
        liveries=["VANILLA", "STOCK_STANDARD", "CLASSIC_LINES", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectroDieselEngineUnit",
        weight=70,
        vehicle_length=6,
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """The Boosters needed a boost. Rebuilt, repainted, off to the races we go."""
    )
    model_def.define_foamer_facts("""BR Class 74, Class 73""")

    result.append(model_def)

    return result
