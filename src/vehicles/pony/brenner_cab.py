from train.factory import ModelDef

# pax capacity on these limits use for 100% mail consists - use the Skeiron for that?


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="TGVCabEngine",
        base_id="brenner_cab",
        base_numeric_id=17090,
        name="Brenner",
        subrole="very_high_speed",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "AC": 3000,
        },
        gen=6,
        intro_year_offset=-14,  # introduce earlier than gen epoch by design, similar to Skeiron
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit",
        weight=52,
        capacity=24,
        spriterow_num=0,
        chassis="4_axle_solid_express_32px",
        tail_light="very_high_speed_32px_2",
    )

    model_def.define_description("""And you shall know this velocity.""")
    model_def.define_foamer_facts("""Alstom Class 390 <i>Pendolino</i>""")

    result.append(model_def)

    return result
