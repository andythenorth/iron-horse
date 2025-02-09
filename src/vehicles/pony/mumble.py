from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineRailbusConsist",
        id="mumble",
        base_numeric_id=830,
        name="Mumble",
        subrole="pax_railbus",
        subrole_child_branch_num=1,
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 400,
        },
        gen=3,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        pax_car_capacity_type="railbus_combine_ng_1",  # specific to combined mail + pax model type
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselRailcarCombineUnitMail",
        weight=18,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_20px",
        tail_light="railcar_20px_1",
    )

    model_def.add_unit_def(
        class_name="DieselRailcarCombineUnitPax",
        weight=18,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_20px",
        tail_light="railcar_20px_1",
    )

    model_def.define_description(
        """Vitesse. Confort. Exactitude. This railcar has none of those. But it is cheap to run."""
    )
    model_def.define_foamer_facts("""Corsican CFC Autorail Billard, CFC X2000/X5000""")

    result.append(model_def)

    return result
