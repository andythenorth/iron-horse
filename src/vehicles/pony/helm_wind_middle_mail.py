from train import TGVMiddleMailEngineConsist, ElectricHighSpeedMailUnit


def main(roster_id, **kwargs):
    consist = TGVMiddleMailEngineConsist(
        roster_id=roster_id,
        id="helm_wind_middle_mail",
        base_numeric_id=6740,
        name="Helm Wind Mail Van",
        role="very_high_speed",
        power_by_power_source={
            "AC": 0
        },  # set power 0, when attached to correct cab, cab power will be increased
        # no pantographs for Helm Wind middle cars
        gen=5,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricHighSpeedMailUnit,
        weight=42,
        spriterow_num=0,
        chassis="4_axle_solid_express_32px",
        repeat=2,
        effects={}, # suppress visual effects
    )

    consist.description = """Can we get there faster? That's what drives me."""
    consist.foamer_facts = (
        """BR InterCity 225 (Mk4 Coaches)), Shinkansen-style distributed traction"""
    )

    return consist
