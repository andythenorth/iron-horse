from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="PassengerEngineRailcarConsist",
        id="breeze",
        base_numeric_id=21850,
        name="Breeze",
        subrole="pax_railcar",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 520,
        },
        pantograph_type="z-shaped-single-with-base",
        easter_egg_haulage_speed_bonus=True,
        gen=5,
        sprites_complete=True,
        intro_year_offset=-3,  # introduce early by design
    )

    model_type_factory.define_unit(
        class_name="ElectricRailcarPaxUnit",
        weight=38,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
    )

    model_type_factory.define_description("""So Swiftly Home""")
    model_type_factory.define_foamer_facts("""BR Class 319, Class 455""")

    result.append(model_type_factory)

    return result
