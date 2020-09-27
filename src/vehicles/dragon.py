from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='dragon',
                            base_numeric_id=420,
                            name='Dragon',
                            role='heavy_express',
                            role_child_branch_num=2,
                            power=2750,
                            random_reverse=True,
                            gen=4,
                            intro_date_offset=1,  # introduce later than gen epoch by design
                            fixed_run_cost_points=240, # give a serious malus to this one (balancing eh?)
                            default_livery_extra_docs_examples=[('COLOUR_BLUE', 'COLOUR_WHITE'), ('COLOUR_PINK', 'COLOUR_WHITE'), ('COLOUR_PALE_GREEN', 'COLOUR_WHITE'), ('COLOUR_CREAM', 'COLOUR_YELLOW')],
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=99,
                     vehicle_length=8,
                     effect_offsets=[(-1, 0), (1, 0)], # double the smoke eh?
                     spriterow_num=0)

    consist.description = """A right big fast diesel hydraulic this one is."""
    consist.foamer_facts = """BR Class 52 <i>Western</i>, BR Class 42/43 <i>Warship</i>."""

    return consist
