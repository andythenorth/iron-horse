from train import (
    PassengerEngineExpressRailcarConsist,
    ElectroDieselExpressRailcarPaxUnit,
)


def main(roster_id, **kwargs):
    consist = PassengerEngineExpressRailcarConsist(
        roster_id=roster_id,
        id="nimbus",
        base_numeric_id=940,
        name="Nimbus",
        role="express_pax_railcar",  # quite a specific role, may or may not scale to other rosters
        role_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 1500,
            "AC": 2500,
        },
        intro_year_offset=-9,  # let's be a little bit earlier for this one - keep match to HST coaches
        gen=6,
        pantograph_type="z-shaped-double-with-base",
        lgv_capable=True,  # for lolz
        tilt_bonus=True,  # for lolz
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectroDieselExpressRailcarPaxUnit,
        weight=60,
        capacity=24,
        chassis="railcar_32px",
        tail_light="railcar_32px_5",
        suppress_roof_sprite=True,
        repeat=2,
    )

    consist.description = """Bridging realms of power. Diesel heart and electric soul. Whispers through dawn's light."""
    consist.foamer_facts = """Bombardier Class 221 <i>Super Voyager</i>, Hitachi Class 800 <i>Intercity Express Train</i>"""

    return consist
