from train import TGVCabEngineConsist, ElectricEngineUnit

# skeiron does not have pax capacity, so it can be used for pure mail consists


def main(roster_id):
    consist = TGVCabEngineConsist(
        roster_id=roster_id,
        id="skeiron_cab",
        base_numeric_id=10000,
        name="Skeiron",
        role="very_high_speed",
        role_child_branch_num=2,
        pantograph_type="z-shaped-single",
        power_by_power_source={
            "AC": 3200,  # more than Brenner, but Brenner has pax capacity
        },
        gen=6,
        intro_year_offset=-14,  # introduce earlier than gen epoch by design, similar to Brenner
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH", "WHITE_STRIPE"],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit,
        weight=54,
        spriterow_num=0,
        chassis="4_axle_solid_express_32px",
        tail_light="very_high_speed_32px_3",
    )

    consist.description = """."""
    consist.foamer_facts = """Alstom Class 373 <i>Eurostar</i>"""

    return consist
