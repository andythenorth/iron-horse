from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="TGVCabEngine",
        model_id="rapide_cab",
        base_numeric_id=28520,
        name="Rapide",
        subrole="very_high_speed",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "OHLE": 1900,
        },
        pantograph_type="z-shaped-single",
        gen=5,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        liveries=["VANILLA", "VANILLA", "VANILLA"],
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

    model_def.define_description("""""")
    model_def.define_foamer_facts(
        """TGV Sud-Est, with TGV 001-style distributed traction"""
    )

    result.append(model_def)

    return result
