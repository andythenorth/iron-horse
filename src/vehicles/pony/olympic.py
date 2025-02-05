from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="PassengerEngineExpressRailcarConsist",
        id="olympic",
        base_numeric_id=900,
        name="Olympic",
        subrole="express_pax_railcar",
        subrole_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={
            "AC": 2200,
        },
        pantograph_type="z-shaped-single-with-base",
        gen=5,
        intro_year_offset=1,  # introduce later by design
        liveries="gen_5_and_6_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="ElectricExpressRailcarPaxUnit",
        weight=46,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    model_type_factory.define_description(
        """Faster with control. Always faster. Always control."""
    )
    model_type_factory.define_foamer_facts("""BR Class 442 <i>Wessex Express</i>""")

    result.append(model_type_factory)

    return result
