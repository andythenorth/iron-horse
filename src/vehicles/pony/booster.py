from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="booster",
        base_numeric_id=21760,
        name="Booster",
        subrole="branch_express",
        subrole_child_branch_num=2,
        power_by_power_source={"DIESEL": 600, "OHLE": 1600},
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=4,
        intro_year_offset=7,  # introduce later than gen epoch by design
        liveries=["STOCK_STANDARD"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ElectroDieselEngineUnit",
        weight=70,
        vehicle_length=6,
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """I've rebuilt some of the Argus fleet to be more handy. Now we're sucking diesel."""
    )
    model_def.define_foamer_facts("""BR Class 71/74, Class 73""")

    result.append(model_def)

    return result
