from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="TGVMiddleMailEngineConsist",
        id="rapide_middle_mail",
        base_numeric_id=6400,
        name="Rapide Mail Van",
        subrole="very_high_speed",
        power_by_power_source={
            "AC": 0
        },  # set power 0, when attached to correct cab, cab power will be increased
        # no pantographs for Alizé middle cars
        gen=5,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="ElectricHighSpeedMailUnit",
        weight=42,
        spriterow_num=0,
        chassis="jacobs_solid_express_32px",
        repeat=2,
        effects={}, # suppress visual effects
    )

    consist_factory.description = """"""
    consist_factory.foamer_facts = """TGV Sud-Est, with TGV 001-style distributed traction"""

    return consist_factory
