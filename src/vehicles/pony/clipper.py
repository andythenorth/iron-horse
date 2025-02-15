from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineRailbus",
        base_id="clipper",
        base_numeric_id=250,
        name="Clipper",
        subrole="pax_railbus",
        subrole_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={
            "DIESEL": 300,
        },
        gen=4,
        # introduce early by design
        intro_year_offset=-4,
        pax_car_capacity_type="railbus_combine",  # specific to combined mail + pax model type
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselRailcarCombineUnitMail",
        weight=18,
        chassis="railbus_swb_20px",
        tail_light="railcar_20px_1",
    )

    model_def.add_unit_def(
        class_name="DieselRailcarCombineUnitPax",
        weight=18,
        chassis="railbus_swb_20px",
        tail_light="railcar_20px_1",
    )

    model_def.define_description(
        """The horses of hope gallop, but the donkeys of experience go slowly."""
    )
    model_def.define_foamer_facts(
        """BR 1st generation AC Cars/Wickham/Waggon-und Maschinenbau and similar railbuses"""
    )

    result.append(model_def)

    return result
