from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="stoat",
        base_numeric_id=21480,
        name="Stoat",
        subrole="branch_freight",
        subrole_child_branch_num=-4,
        power_by_power_source={
            "OHLE": 1050,
        },
        speed=60,  # continues a long way into gen 3, so go faster
        random_reverse=True,
        pantograph_type="diamond-single",
        gen=2,
        intro_year_offset=3,  # introduce later than gen epoch by design
        extended_vehicle_life=True,
        fixed_run_cost_points=105,  # substantial cost bonus so it can make money
        liveries=["LOWER_LINES", "BANGER_BLUE", "FREIGHT_BLACK", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ElectricEngineUnit",
        weight=54,
        vehicle_length=6,
        rel_spriterow_index=0,
    )

    model_def.define_description("""Nippy little bugger.""")
    model_def.define_foamer_facts(
        """NER ES1, Metropolitan Railway camel-back and box-cab locomotives, Westoe Colliery electrics, generic steeple-cab locomotives"""
    )

    result.append(model_def)

    return result
