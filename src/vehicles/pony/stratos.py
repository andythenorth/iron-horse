from train import (
    PassengerEngineExpressRailcarConsist,
    DieselExpressRailcarPaxUnit,
)


def main(roster_id, **kwargs):
    consist = PassengerEngineExpressRailcarConsist(
        roster_id=roster_id,
        id="stratos",
        base_numeric_id=390,
        name="Stratos",
        role="express_pax_railcar",  # quite a specific role, may or may not scale to other rosters
        role_child_branch_num=-2,
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 1200,  # corsica AMG 800 is 590hp per engine https://fr.wikipedia.org/wiki/AMG_800
        },
        gen=4,
        tilt_bonus=True,  # for lolz
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        consist_ruleset="railcars_4_unit_sets",  # special case
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselExpressRailcarPaxUnit,
        weight=50,
        capacity=24,
        chassis="railcar_ng_32px",
        tail_light="railcar_32px_6",
        suppress_roof_sprite=True,
        repeat=2,
    )

    consist.description = """Every journey becomes a panorama."""
    consist.foamer_facts = """Corsican AMG 800"""

    return consist
