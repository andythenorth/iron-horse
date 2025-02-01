from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="TGVMiddleMailEngineConsist",
        id="brenner_middle_mail",
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

    consist_factory.add_unit(
        class_name="ElectricHighSpeedMailUnit",
        weight=52,
        spriterow_num=0,
        chassis="jacobs_solid_express_32px",
        repeat=2,
        effects={},  # suppress visual effects
    )

    consist_factory.add_description("""And you shall know this velocity.""")
    consist_factory.add_foamer_facts("""Alstom Class 390 <i>Pendolino</i>""")

    result.append(consist_factory)

    return result
