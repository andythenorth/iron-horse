from train import EngineConsist, DieselEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="rockhampton",
        base_numeric_id=21290,
        name="Rockhampton",
        subrole="universal",
        subrole_child_branch_num=-4,
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 1200,
        },
        gen=3,
        intro_year_offset=4,  # introduce a bit later
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        random_reverse=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=55,
        vehicle_length=8,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    # various NZ / tasrail / QLD diesels
    # but could have been entirely different - https://en.wikipedia.org/wiki/Euskotren_TD2000_series
    consist.description = (
        """From down under emerges a tiny colossus. Footsure, flexible and all grunt."""
    )
    consist.foamer_facts = """New Zealand Railways DJ class (Mitsubishi bo-bo-bo)"""

    return consist
