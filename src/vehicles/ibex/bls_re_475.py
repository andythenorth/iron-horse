from train.factory import ModelDef

# multi-system !!


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="bls_re_475",
        base_numeric_id=30790,
        name="BLS Re 475 !! Multi-system",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 7400,
            "DC": 7400,
        },
        random_reverse=True,
        gen=6,
        pantograph_type="diamond-double",
        intro_year_offset=12,  # introduce later than gen epoch by design
        liveries=["VANILLA"],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit",
        weight=105,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description(""" """)
    model_def.define_foamer_facts("""BLS Re 475 (Vectron)""")

    result.append(model_def)

    return result
