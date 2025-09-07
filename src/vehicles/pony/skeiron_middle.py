from train.factory import ModelDef

# !! can we do both middle parts in one module?


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="TGVMiddlePassengerEngine",
        model_id="skeiron_middle_passenger",
        cab_id="skeiron_cab",
        base_numeric_id=420,
        name="Skeiron Passenger Coach",
        subrole="very_high_speed",
        power_by_power_source={
            "OHLE": 0
        },  # set power 0, when attached to correct cab, cab power will be increased
        gen=6,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricHighSpeedPaxUnit",
        weight=54,
        rel_spriterow_index=0,
        chassis="jacobs_solid_express_32px",
        repeat=2,
        effects={},  # suppress visual effects
    )

    model_def.define_description(""".""")
    model_def.define_foamer_facts(""" """)

    result.append(model_def)

    model_def = ModelDef(
        class_name="TGVMiddleMailEngine",
        model_id="skeiron_middle_mail",
        cab_id="skeiron_cab",
        base_numeric_id=430,
        name="Skeiron Mail Van",
        subrole="very_high_speed",
        power_by_power_source={
            "OHLE": 0
        },  # set power 0, when attached to correct cab, cab power will be increased
        gen=6,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricHighSpeedMailUnit",
        weight=54,
        rel_spriterow_index=0,
        chassis="jacobs_solid_express_32px",
        repeat=2,
        effects={},  # suppress visual effects
    )

    model_def.define_description(""".""")
    model_def.define_foamer_facts(""" """)

    result.append(model_def)

    return result
