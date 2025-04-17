from train.factory import ModelDef

# !! can we do both middle parts in one module?

def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="TGVMiddleMailEngine",
        model_id="brenner_middle_mail",
        cab_id="brenner_cab",
        base_numeric_id=6780,
        name="Brenner Mail Van",
        subrole="very_high_speed",
        pantograph_type="z-shaped-single-with-base",
        power_by_power_source={
            "AC": 0
        },  # set power 0, when attached to correct cab, cab power will be increased
        gen=6,
        intro_year_offset=-14,  # introduce earlier than gen epoch by design
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricHighSpeedMailUnit",
        weight=52,
        rel_spriterow_index=0,
        chassis="jacobs_solid_express_32px",
        repeat=2,
        effects={},  # suppress visual effects
    )

    model_def.define_description("""And you shall know this velocity.""")
    model_def.define_foamer_facts("""Alstom Class 390 <i>Pendolino</i>""")

    result.append(model_def)

    return result
