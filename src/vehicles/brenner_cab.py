from train import TGVCabEngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = TGVCabEngineConsist(
        roster_id=roster_id,
        id="brenner_cab",
        base_numeric_id=9170,
        name="Brenner",
        role="very_high_speed",
        role_child_branch_num=1,
        dual_headed=True,
        power_by_power_source={
            "AC": 3000,
        },
        gen=6,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        additional_liveries=["SWOOSH"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricEngineUnit,
        weight=52,
        spriterow_num=0,
        chassis="4_axle_solid_express_32px",
        tail_light="very_high_speed_32px_2",
    )

    consist.description = """And you shall know this velocity."""
    consist.foamer_facts = """Alstom Class 390 <i>Pendolino</i>"""

    return consist
