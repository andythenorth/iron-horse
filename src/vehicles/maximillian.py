from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="maximillian",
        base_numeric_id=14950,
        name="Maximillian",
        role="universal",
        role_child_branch_num=2,
        power_by_power_source={
            "DIESEL": 900,
        },
        random_reverse=True,
        base_track_type_name="NG",
        gen=4,
        intro_year_offset=10,
        # banger blue?
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=31,
        vehicle_length=6,
        effect_z_offset=9,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist.description = """The ultimate narrow gauge diesel."""
    consist.foamer_facts = (
        """CFD Locotracteur BB-400, South African 'Funkey' diesels, FAUR L45H B-B"""
    )

    return consist
