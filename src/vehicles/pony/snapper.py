from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineRailbusConsist",
        id="snapper",
        base_numeric_id=9350,
        name="Snapper",
        subrole="pax_railbus",
        subrole_child_branch_num=1,
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 560,
        },
        gen=4,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        pax_car_capacity_type="railbus_combine_ng_1",  # specific to combined mail + pax model type
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselRailcarCombineUnitMail",
        weight=22,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_20px",
        tail_light="railcar_20px_1",
    )

    model_def.add_unit_def(
        class_name="DieselRailcarCombineUnitPax",
        weight=22,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_20px",
        tail_light="railcar_20px_1",
    )

    model_def.define_description(
        """A better railcar, for a new narrow-gauge century."""
    )
    model_def.define_foamer_facts("""Corsican CFC X2000/X5000, CFD Autorails""")

    result.append(model_def)

    return result
