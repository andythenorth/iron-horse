from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="TGVCabEngine",
        model_id="alize_cab",
        base_numeric_id=17100,
        name="Alizé",
        subrole="very_high_speed",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "OHLE": 1900,
        },
        pantograph_type="z-shaped-single",
        gen=5,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        liveries=["SURE_PACE", "SHOW_PONY", "MAIL_BY_RAIL"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ElectricEngineUnit",
        weight=76,
        # no pax capacity on Helm Wind cabs
        capacity=0,
        rel_spriterow_index=0,
        chassis="4_axle_solid_express_32px",
        tail_light="very_high_speed_32px_3",
    )

    model_def.define_description(
        """Whispers in the wind. Graceful as she slices air. Swift, pure, and untamed."""
    )
    model_def.define_foamer_facts(
        """TGV Sud-Est, with TGV 001-style distributed traction"""
    )

    result.append(model_def)

    return result
