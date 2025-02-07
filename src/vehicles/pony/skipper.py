from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_def = ModelTypeFactory(
        class_name="PassengerEngineRailbusConsist",
        id="skipper",
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

    model_def.define_unit(
        class_name="DieselRailcarCombineUnitMail",
        weight=20,
        chassis="railbus_lwb_20px",
        tail_light="railcar_20px_1",
    )

    model_def.define_unit(
        class_name="DieselRailcarCombineUnitPax",
        weight=20,
        chassis="railbus_lwb_20px",
        tail_light="railcar_20px_2",
    )

    model_def.define_description("""Patience is the virtue of the donkeys.""")
    model_def.define_foamer_facts("""BR Class 141/142/143/144 <i>Pacers</i>""")

    result.append(model_def)

    return result
