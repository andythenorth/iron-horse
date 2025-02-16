from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineRailbus",
        model_type_id="zipper",
        base_numeric_id=260,
        name="Zipper",
        subrole="pax_railbus",
        subrole_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={
            "DIESEL": 480,
        },
        gen=6,
        # introduce early by design
        intro_year_offset=-4,
        pax_car_capacity_type="railbus_combine",  # specific to combined mail + pax model type
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselRailcarCombineUnitMail",
        weight=21,
        chassis="railbus_lwb_20px",
        tail_light="railcar_20px_1",
    )

    model_def.add_unit_def(
        class_name="DieselRailcarCombineUnitPax",
        weight=21,
        chassis="railbus_lwb_20px",
        tail_light="railcar_20px_1",
    )

    model_def.define_description("""It's the same donkey, but with a new saddle.""")
    model_def.define_foamer_facts("""BR Class 144e <i>Pacer</i>, Vivarail D-Train""")

    result.append(model_def)

    return result
