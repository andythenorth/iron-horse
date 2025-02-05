from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="EngineConsist",
        id="bb_8500_duo",
        base_numeric_id=200,
        name="BB 8500 / 16000 (duo)",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=-3,
        power_by_power_source={"DC": 10700},
        gen=5,
        pantograph_type="diamond-double",
        intro_year_offset=8,  # introduce later than gen epoch by design
        sprites_complete=False,
    )

    model_type_factory.define_unit(
        class_name="ElectricEngineUnit",
        weight=105,
        vehicle_length=6,
        spriterow_num=0,
        repeat=2,
    )

    model_type_factory.define_description(""" """)
    model_type_factory.define_foamer_facts("""SNCF BB 8500 / 16000 (duo)""")

    result.append(model_type_factory)

    return result
