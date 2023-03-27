from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="toaster",
        base_numeric_id=13840,
        name="Toaster",
        role="super_heavy_freight",
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 3750,
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.38,
        random_reverse=True,
        gen=6,
        # introduce early by design
        intro_year_offset=-10,
        fixed_run_cost_points=220,  # unrealism: run cost nerf for being so high-powered
        default_livery_extra_docs_examples=[
            ("COLOUR_GREEN", "COLOUR_YELLOW"),
            ("COLOUR_PALE_GREEN", "COLOUR_YELLOW"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=130,
        vehicle_length=8,
        effect_offsets=[(1, 0)],
        spriterow_num=0,
    )

    consist.description = (
        """I've heard these might catch fire, but we're getting them cheap."""
    )
    consist.foamer_facts = """GE Class 70 <i>Powerhaul</i>"""

    return consist
