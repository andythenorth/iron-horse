from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='streamer',
                            base_numeric_id=4840,
                            name='2-6-2 Streamer',
                            role='heavy_express',
                            role_child_branch_num=-2, # -ve because Joker
                            replacement_consist_id='dragon', # this Joker ends with Dragon
                            power=1850, # slightly less than Strongbow (and lighter engine)
                            tractive_effort_coefficient=0.18,
                            gen=3,
                            intro_date_offset=4, # introduce later than gen epoch by design
                            default_livery_extra_docs_examples=[('COLOUR_DARK_GREEN', 'COLOUR_DARK_GREEN'), ('COLOUR_GREY', 'COLOUR_WHITE'), ('COLOUR_WHITE', 'COLOUR_BLUE')],
                            sprites_complete=True)

    consist.add_unit(type=SteamEngineUnit,
                     weight=85,
                     vehicle_length=7,
                     effect_offsets=[(-3, 0), (-2, 0)], # double the smoke eh?
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=36,
                     vehicle_length=3,
                     spriterow_num=1)

    consist.description = """Mr. Gresley did these. I'm sure he knows what he's doing."""
    consist.foamer_facts = """LNER V2, LNER streamlined B17/A4/P2."""

    return consist
