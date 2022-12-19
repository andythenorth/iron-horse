from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="highlander",
        base_numeric_id=13290,
        name="Highlander",
        role="super_heavy_freight",
        role_child_branch_num=2,
        power_by_power_source={
            "DIESEL": 4550,  # 900hp steps Revolution -> Blackthorn -> Toaster
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.4,
        random_reverse=True,
        intro_year_offset=-1,  # let's be a little bit earlier for this one
        gen=6,
        fixed_run_cost_points=220,  # unrealism: run cost nerf for being so high-powered
        additional_liveries=["FREIGHTLINER_GBRF"],
        default_livery_extra_docs_examples=[
            ("COLOUR_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_YELLOW"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=128,
        vehicle_length=8,
        effect_offsets=[(1, 0)],
        spriterow_num=0,
    )

    consist.description = """A bigger Cheddar Valley, what's not to like about it?"""
    consist.foamer_facts = (
        """modernised GMD / EMD Class 59, uprated GMD / EMD 710 series prime mover"""
    )

    return consist
