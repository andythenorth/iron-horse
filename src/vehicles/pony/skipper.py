from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineRailbus",
        model_id="skipper",
        base_numeric_id=240,
        name="Skipper",
        subrole="pax_railbus",
        subrole_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={
            "DIESEL": 400,
        },
        gen=5,
        # introduce early by design
        intro_year_offset=-4,
        pax_car_capacity_type="railbus_combine",  # specific to combined mail + pax model type
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselRailcarCombineUnitMail",
        weight=20,
        chassis="railbus_lwb_20px",
        tail_light="railcar_20px_1",
    )

    model_def.add_unit_def(
        class_name="DieselRailcarCombineUnitPax",
        weight=20,
        chassis="railbus_lwb_20px",
        tail_light="railcar_20px_2",
    )

    model_def.define_description("""Patience is the virtue of the donkeys.""")
    model_def.define_foamer_facts("""BR Class 141/142/143/144 <i>Pacers</i>""")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerEngineRailbus",
        model_id="skipper_single",
        base_numeric_id=22290,
        name="Skipper",
        subrole="pax_railbus",
        subrole_child_branch_num=-3000,  # excessive child branch number to hide them from tech tree (and also -ve to hide in simplified mode)
        power_by_power_source={
            "DIESEL": 225,
        },
        gen=5,
        # introduce early by design
        intro_year_offset=-4,
        # match to equivalent twin-unit railbus id
        vehicle_family_id="skipper",
        # it's too complex to clone these from the twin unit, but treat the result like a clone
        quacks_like_a_clone=True,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselRailcarPaxUnit",
        weight=24,
        chassis="railbus_lwb_24px",
        tail_light="railcar_24px_1",
    )

    model_def.define_description("""Patience is the virtue of the donkeys.""")
    model_def.define_foamer_facts("""BR Class 141/142/143/144 <i>Pacers</i>""")

    result.append(model_def)

    return result
