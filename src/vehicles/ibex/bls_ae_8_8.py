from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="EngineConsist",
        id="bls_ae_8_8",
        base_numeric_id=130,
        name="BLS Ae 8/8",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=3,
        power_by_power_source={
            "AC": 8700,
        },
        gen=3,
        pantograph_type="diamond-double",
        # intro_year_offset=-13,  # introduce earlier than gen epoch by design
        sprites_complete=False,
    )

    model_type_factory.define_unit(
        class_name="ElectricEngineUnit",
        weight=75,
        vehicle_length=6,
        spriterow_num=0,
        repeat=2,
    )

    model_type_factory.define_description(""" """)
    model_type_factory.define_foamer_facts("""BLS Ae 8/8""")

    result.append(model_type_factory)

    return result
