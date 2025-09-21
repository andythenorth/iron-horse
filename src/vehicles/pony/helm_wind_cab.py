from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="TGVCabEngine",
        model_id="helm_wind_cab",
        base_numeric_id=22330,
        name="Helm Wind",
        subrole="very_high_speed",
        subrole_child_branch_num=1,
        power_by_power_source={
            "OHLE": 1900,
        },
        pantograph_type="z-shaped-single-reversed",
        gen=5,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        liveries=["INTERCITY_RASPBERRY_RIPPLE", "WHITE_STRIPE"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit",
        weight=76,
        # no pax capacity on Helm Wind cabs
        capacity=0,
        rel_spriterow_index=0,
        chassis="4_axle_solid_express_32px",
        tail_light="very_high_speed_32px_1",
    )

    model_def.define_description("""Can we get there faster? That's what drives me.""")
    model_def.define_foamer_facts(
        """BR InterCity 225 (Class 91), BR APT-P, Shinkansen-style distributed traction"""
    )

    result.append(model_def)

    return result
