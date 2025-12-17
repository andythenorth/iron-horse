from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="FixedFormationRailcarCombineEngine",
        model_id="golfinho",
        base_numeric_id=970,
        name="Golfinho",
        subrole="pax_railbus",
        subrole_child_branch_num=-2,
        base_track_type="NG",
        power_by_power_source={
            "DIESEL": 900,
        },
        gen=4,
        fixed_run_cost_points=20,  # balance against Snapper
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        pax_car_capacity_type="railbus_combine_ng_2",  # specific to combined mail + pax model type
        liveries=["SHOW_PONY"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="DieselRailcarCombineUnitPax",
        weight=20,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_20px",
        tail_light="railcar_20px_3",
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        unit_cls_name="DieselRailcarCombineUnitPax",
        weight=22,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_24px",
        rel_spriterow_index=1,
    )

    model_def.add_unit_def(
        unit_cls_name="DieselRailcarCombineUnitMail",
        weight=20,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_20px",
        tail_light="railcar_20px_3",
        rel_spriterow_index=0,
        reverse_sprite_template=True,
    )

    model_def.define_description(
        """Efficiently whisking passengers about in the most modern ways. Goats remain, at this time, disallowed."""
    )
    model_def.define_foamer_facts("""Stadler SPATZ""")

    result.append(model_def)

    return result
