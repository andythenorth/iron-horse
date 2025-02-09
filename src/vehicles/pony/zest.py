from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="zest",
        base_numeric_id=21770,
        name="Zest",
        subrole="branch_freight",
        subrole_child_branch_num=-3,
        power_by_power_source={
            "AC": 1600,
        },
        speed=87,  # continues past gen 5, so go faster
        random_reverse=True,
        pantograph_type="diamond-single",
        gen=4,
        intro_year_offset=6,  # introduce later than gen epoch by design
        extended_vehicle_life=True,
        fixed_run_cost_points=105,  # substantial cost bonus so it can make money
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit", weight=54, vehicle_length=6, spriterow_num=0
    )

    model_def.define_description("""Solid unit.""")
    model_def.define_foamer_facts(
        """Modernised NER ES1, Metropolitan Railway camel-back and box-cab locomotives, Westoe Colliery electrics, generic steeple-cab locomotives"""
    )

    result.append(model_def)

    return result
