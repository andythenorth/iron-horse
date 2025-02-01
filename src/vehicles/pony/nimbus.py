from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="PassengerEngineExpressRailcarConsist",
        id="nimbus",
        base_numeric_id=940,
        name="Nimbus",
        subrole="express_pax_railcar",  # quite a specific role, may or may not scale to other rosters
        subrole_child_branch_num=-2,
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

    consist_factory.add_unit(
        class_name="ElectroDieselExpressRailcarPaxUnit",
        weight=60,
        capacity=24,
        chassis="railcar_32px",
        tail_light="railcar_32px_5",
        suppress_roof_sprite=True,
        repeat=2,
    )

    consist_factory.add_description(
        """Bridging realms of power. Diesel heart and electric soul. Whispers through dawn's light."""
    )
    consist_factory.add_foamer_facts(
        """Bombardier Class 221 <i>Super Voyager</i>, Hitachi Class 800 <i>Intercity Express Train</i>"""
    )

    return consist_factory
