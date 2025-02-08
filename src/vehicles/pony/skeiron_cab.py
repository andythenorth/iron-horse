from train import ModelDef

# skeiron does not have pax capacity, so it can be used for pure mail consists


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="TGVCabEngineConsist",
        id="skeiron_cab",
        base_numeric_id=25120,
        name="Skeiron",
        subrole="very_high_speed",
        subrole_child_branch_num=2,
        pantograph_type="z-shaped-single",
        power_by_power_source={
            "AC": 3200,  # more than Brenner, but Brenner has pax capacity
        },
        gen=6,
        intro_year_offset=-14,  # introduce earlier than gen epoch by design, similar to Brenner
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH", "WHITE_STRIPE"],
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="ElectricEngineUnit",
        weight=54,
        spriterow_num=0,
        chassis="4_axle_solid_express_32px",
        tail_light="very_high_speed_32px_3",
    )

    model_def.define_description(
        """Myth in motion, swift. Continents woven in speed. Elegance entwined."""
    )
    model_def.define_foamer_facts("""Alstom Class 373 <i>Eurostar</i>""")

    result.append(model_def)

    return result
