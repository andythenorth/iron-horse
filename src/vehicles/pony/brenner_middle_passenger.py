from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="TGVMiddlePassengerEngineConsist",
        id="brenner_middle_passenger",
        base_numeric_id=2880,
        name="Brenner Passenger Coach",
        subrole="very_high_speed",
        pantograph_type="z-shaped-single-with-base",
        power_by_power_source={
            "AC": 0
        },  # set power 0, when attached to correct cab, cab power will be increased
        gen=6,
        intro_year_offset=-14,  # introduce earlier than gen epoch by design
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="ElectricHighSpeedPaxUnit",
        weight=52,
        spriterow_num=0,
        chassis="jacobs_solid_express_32px",
        repeat=2,
        effects={},  # suppress visual effects
    )

    model_def.define_description("""And you shall know this velocity.""")
    model_def.define_foamer_facts("""Alstom Class 390 <i>Pendolino</i>""")

    result.append(model_def)

    return result
