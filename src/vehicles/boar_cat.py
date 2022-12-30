from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="boar_cat",
        base_numeric_id=10360,
        name="Boar Cat",
        role="universal",
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 600,
        },
        random_reverse=True,
        base_track_type_name="NG",
        gen=4,
        # banger blue?
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=23,
        vehicle_length=4,
        effect_z_offset=9,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist.description = """This is a big small cat."""
    consist.foamer_facts = (
        """CFD Locotracteur BB-400, South African 'Funkey' diesels, FAUR L45H B-B"""
    )

    return consist
