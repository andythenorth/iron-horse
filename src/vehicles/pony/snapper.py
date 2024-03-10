from train import PassengerEngineRailbusConsist, DieselRailcarCombineUnitMail, DieselRailcarCombineUnitPax


def main(roster_id, **kwargs):
    consist = PassengerEngineRailbusConsist(
        roster_id=roster_id,
        id="snapper",
        base_numeric_id=9350,
        name="Snapper",
        role="pax_railbus",
        role_child_branch_num=1,
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 560,
        },
        gen=4,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        pax_car_capacity_type="railbus_combine_ng_1",  # specific to combined mail + pax consist
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselRailcarCombineUnitMail,
        weight=22,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_20px",
        tail_light="railcar_20px_1",
    )

    consist.add_unit(
        type=DieselRailcarCombineUnitPax,
        weight=22,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_20px",
        tail_light="railcar_20px_1",
    )

    consist.description = """A better railcar, for a new narrow-gauge century."""
    consist.foamer_facts = """Corsican CFC X2000/X5000, CFD Autorails"""

    return consist
