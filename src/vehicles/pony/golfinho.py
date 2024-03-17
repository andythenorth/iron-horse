from train import FixedFormationRailcarCombineConsist, DieselRailcarCombineUnitMail, DieselRailcarCombineUnitPax

def main(roster_id, **kwargs):
    consist = FixedFormationRailcarCombineConsist(
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
        fixed_run_cost_points=20, # balance against Snapper
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        pax_car_capacity_type="railbus_combine_ng_2",  # specific to combined mail + pax consist
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselRailcarCombineUnitPax,
        weight=20,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_20px",
        tail_light="railcar_20px_3",
        spriterow_num=0,
    )

    consist.add_unit(
        type=DieselRailcarCombineUnitPax,
        weight=22,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_24px",
        spriterow_num=1,
    )

    consist.add_unit(
        type=DieselRailcarCombineUnitMail,
        weight=20,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_20px",
        tail_light="railcar_20px_3",
        spriterow_num=0,
        reverse_sprite_template=True,
    )

    consist.description = """Efficiently whisking passengers about in the most modern ways. Goats remain, at this time, disallowed."""
    consist.foamer_facts = """Stadler SPATZ"""

    return consist
