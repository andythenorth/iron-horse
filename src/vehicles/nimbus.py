from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="nimbus",
        base_numeric_id=14540,
        name="Nimbus",
        role="super_heavy_express",
        role_child_branch_num=-3,
        power_by_power_source={
            "AC": 5400,  # needs a bump from Screamer
        },
        random_reverse=True,
        gen=6,
        pantograph_type="z-shaped-double",
        intro_year_offset=3,  # introduce later than gen epoch by design
        force_default_pax_mail_livery=2,  # pax/mail cars default to second livery with this engine
        additional_liveries=["FREIGHTLINER_GBRF"],
        default_livery_extra_docs_examples=[
            ("COLOUR_WHITE", "COLOUR_BLUE"),
            ("COLOUR_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PINK", "COLOUR_DARK_BLUE"),
            ("COLOUR_WHITE", "COLOUR_RED"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=85, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """I've done a faster Screamer, proven design, no fuss no bother."""
    )
    consist.foamer_facts = """BR Class 90"""

    return consist
