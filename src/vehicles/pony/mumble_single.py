from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineRailbusConsist",
        base_id="mumble_single",
        base_numeric_id=17140,
        name="Mumble",
        subrole="pax_railbus",
        subrole_child_branch_num=-3000,  # excessive child branch number to hide them from tech tree (and also -ve to hide in simplified mode)
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 250,
        },
        gen=3,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        buyable_variant_group_id="mumble",  # for pony, specifically force variant group (parent) to equivalent twin-unit railbus id
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselRailcarPaxUnit",
        weight=18,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_24px",
        tail_light="railcar_24px_1",
    )

    model_def.define_description(
        """Vitesse. Confort. Exactitude. This railcar has none of those. But it is cheap to run."""
    )
    model_def.define_foamer_facts("""Corsican CFC Autorail Billard, CFC X2000/X5000""")

    result.append(model_def)

    return result
