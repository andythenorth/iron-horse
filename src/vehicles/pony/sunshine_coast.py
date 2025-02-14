from train.train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineExpressRailcarConsist",
        base_id="sunshine_coast",
        base_numeric_id=4130,
        name="Sunshine Coast",
        subrole="express_pax_railcar",
        subrole_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={
            "AC": 1900,
        },
        pantograph_type="z-shaped-single-with-base",
        gen=4,
        intro_year_offset=1,  # introduce later by design
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricExpressRailcarPaxUnit",
        weight=45,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    model_def.define_description(
        """Better three hours too soon than a minute too late."""  # Shakespeare
    )
    model_def.define_foamer_facts("""BR Class 309 <i>Clacton Express</i>, BR 4-REP""")

    result.append(model_def)

    return result
