from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="gargouille",
        base_numeric_id=12000,
        name="Gargouille",
        role="universal",
        role_child_branch_num=2,
        power_by_power_source={
            "DIESEL": 900,
        },
        random_reverse=True,
        base_track_type_name="NG",
        gen=3,
        intro_year_offset=11,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW", "BANGER_BLUE", "INDUSTRIAL_YELLOW"], # different body heights, for lolz :P
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=40,
        vehicle_length=6,
        effect_z_offset=9,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist.description = """Le petit train du jour. I've imported a few of these."""
    consist.foamer_facts = (
        """CFD Locotracteur BB-400, South African 'Funkey' diesels, FAUR L45H B-B"""
    )

    return consist
