from train import AutoCoachCombineConsist, DieselRailcarCombineUnitMail, DieselRailcarCombineUnitPax

def main(roster_id, **kwargs):
    consist = AutoCoachCombineConsist(
        roster_id=roster_id,
        id="golfinho",
        base_numeric_id=970,
        name="Golfinho",
        role="pax_railbus",
        role_child_branch_num=-2,
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 900,
        },
        gen=4,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        pax_car_capacity_type="railbus_combine_ng_2",  # specific to combined mail + pax consist
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselRailcarCombineUnitPax,
        weight=18,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_20px",
        tail_light="railcar_24px_1", # !!!!!!!!!!!!!!!!!!!!!!! wrong length
    )

    consist.add_unit(
        type=DieselRailcarCombineUnitMail,
        weight=18,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_24px",
        tail_light="railcar_24px_1", # !!!!!!!!!!!!!!!!!!!!!!! wrong length
    )

    consist.add_unit(
        type=DieselRailcarCombineUnitPax,
        weight=18,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_20px",
        tail_light="railcar_24px_1", # !!!!!!!!!!!!!!!!!!!!!!! wrong length
    )

    #https://fr.wikipedia.org/wiki/Stadler_SPATZ
    consist.description = """Efficiently whisking passengers about in the most modern ways. Goats remain, at this time, disallowed."""
    consist.foamer_facts = """Stadler SPATZ"""

    return consist
