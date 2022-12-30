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
            "DIESEL": 750,
        },
        random_reverse=True,
        base_track_type_name="NG",
        gen=3,
        intro_year_offset=15,
        # banger blue?
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=30,
        vehicle_length=6,
        effect_z_offset=9,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist.description = """Le petit train du jour. I've imported a few of these."""
    consist.foamer_facts = (
        """CFD Locotracteur BB-400, South African 'Funkey' diesels, FAUR L45H B-B"""
    )

    return consist
