from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="streamer",
        base_numeric_id=4840,
        name="4-6-4 Streamer",
        role="super_heavy_express",
        role_child_branch_num=-2,  # -ve because Joker
        power_by_power_source={
            "STEAM": 2300,
        },
        tractive_effort_coefficient=0.18,
        gen=3,
        intro_year_offset=4,  # introduce later than gen epoch by design
        force_default_pax_mail_livery=2,  # pax/mail cars default to second livery with this engine
        default_livery_extra_docs_examples=[
            ("COLOUR_DARK_GREEN", "COLOUR_DARK_GREEN"),
            ("COLOUR_GREY", "COLOUR_WHITE"),
            ("COLOUR_WHITE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=SteamEngineUnit,
        weight=111,
        vehicle_length=8,
        effect_offsets=[(-3, 0), (-2, 0)],  # double the smoke eh?
        spriterow_num=0,
    )

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=39, vehicle_length=4, spriterow_num=1
    )

    consist.description = (
        """Mr. Gresley did these. I'm sure he knows what he's doing."""
    )
    consist.foamer_facts = """LNER W1 'Hush Hush'"""

    return consist
