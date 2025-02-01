from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="toaster",
        base_numeric_id=21510,
        name="Toaster",
        subrole="super_heavy_freight",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 4200,
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.39,
        random_reverse=True,
        gen=6,
        # introduce as gen 6 by design, but then make it early
        intro_year_offset=-15,
        fixed_run_cost_points=220,  # unrealism: run cost nerf for being so high-powered
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        default_livery_extra_docs_examples=[
            ("COLOUR_GREEN", "COLOUR_YELLOW"),
            ("COLOUR_PALE_GREEN", "COLOUR_YELLOW"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit",
        weight=130,
        vehicle_length=8,
        effect_offsets=[(1, 0)],
        spriterow_num=0,
    )

    consist_factory.description = (
        """I've heard these might catch fire, but we're getting them cheap."""
    )
    consist_factory.foamer_facts = """GE Class 70 <i>Powerhaul</i>"""

    return consist_factory
