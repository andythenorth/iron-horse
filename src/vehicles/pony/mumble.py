from train import (
    PassengerEngineRailbusConsist,
    DieselRailcarCombineUnitPax,
    DieselRailcarCombineUnitMail,
)


def main(roster_id, **kwargs):
    consist = PassengerEngineRailbusConsist(
        roster_id=roster_id,
        id="mumble",
        base_numeric_id=830,
        name="Mumble",
        role="pax_railbus",
        role_child_branch_num=1,
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 400,
        },
        gen=3,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        pax_car_capacity_type="railbus_combine_ng_1",  # specific to combined mail + pax consist
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselRailcarCombineUnitMail,
        weight=18,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_20px",
        tail_light="railcar_20px_1",
    )

    consist.add_unit(
        type=DieselRailcarCombineUnitPax,
        weight=18,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_20px",
        tail_light="railcar_20px_1",
    )

    consist.description = """Vitesse. Confort. Exactitude. This railcar has none of those. But it is cheap to run."""
    consist.foamer_facts = """Corsican CFC Autorail Billard, CFC X2000/X5000"""

    return consist
