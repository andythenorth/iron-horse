from train import EngineConsist, ElectroDieselEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="ultra_shoebox",
        base_numeric_id=11210,
        name="Ultra Shoebox",
        role="heavy_express",
        role_child_branch_num=-3,
        power_by_power_source={"DIESEL": 1650, "AC": 2800},
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=5,
        intro_year_offset=6,  # earlier than anything IRL, but we want 125 mph capability so eh, there we go
        extended_vehicle_life=True,  # because long time until replaced
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[],
        default_livery_extra_docs_examples=[
            ("COLOUR_RED", "COLOUR_RED"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
            ("COLOUR_PURPLE", "COLOUR_WHITE"),
            ("COLOUR_CREAM", "COLOUR_MAUVE"),
            ("COLOUR_YELLOW", "COLOUR_YELLOW"),
            ("COLOUR_DARK_BLUE", "COLOUR_BLUE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
        sprites_additional_liveries_potential=True,  # banger blue, yellow? - unused banger blue from Super Shoebox also?  Freightliner swoosh?
    )

    consist.add_unit(
        type=ElectroDieselEngineUnit,
        weight=84,
        vehicle_length=8,
        effect_offsets=[(2, 0)],
        spriterow_num=0,
    )

    consist.description = (
        """Top to bottom, it's an old Shoebox made new. Right powerful small engines."""
    )
    consist.foamer_facts = """Network Rail / GBRF Class 73/9 (re-engineered), BR Class 74, proposed Class 75"""

    return consist
