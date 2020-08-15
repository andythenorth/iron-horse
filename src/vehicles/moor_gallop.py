from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='moor_gallop',
                            base_numeric_id=170,
                            name='Moor Gallop',
                            role='heavy_express',
                            role_child_branch_num=3,
                            power=2400,
                            tractive_effort_coefficient=0.25,
                            random_reverse=True,
                            gen=3,
                            pantograph_type='diamond-double',
                            intro_date_offset=5,  # introduce later than gen epoch by design
                            default_livery_extra_docs_examples=[('COLOUR_LIGHT_BLUE', 'COLOUR_WHITE'), ('COLOUR_PALE_GREEN', 'COLOUR_WHITE'), ('COLOUR_DARK_GREEN', 'COLOUR_WHITE'), ('COLOUR_BLUE', 'COLOUR_BLUE')],
                            sprites_complete=True)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=105,
                     vehicle_length=8,
                     spriterow_num=0)

    consist.description = """It's not so hurly-burly, but it's a nice new electric engine for you."""
    consist.cite = """Mr. Train"""
    consist.foamer_facts = """LNER EM2 (BR Class 77)."""

    return consist
