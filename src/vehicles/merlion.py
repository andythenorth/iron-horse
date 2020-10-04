from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='merlion',
                            base_numeric_id=4920,
                            name='Merlion',
                            role='express',
                            role_child_branch_num=1,
                            #replacement_consist_id='slug', # this Joker ends with Slug
                            power=1750,
                            tractive_effort_coefficient=0.26,
                            fixed_run_cost_points=42, # give a bonus so this can be a genuine mixed-traffic engine
                            random_reverse=True,
                            gen=4,
                            intro_date_offset=-2,  # let's be a littler earlier for this one
                            alternative_cc_livery='RAILFREIGHT_RED_STRIPE',
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=105,
                     vehicle_length=8,
                     effect_offsets=[(2, 0)],
                     spriterow_num=0)

    consist.description = """I don't like the looks of it right much, but I suppose it will do."""
    consist.foamer_facts = """BR Class 31."""

    return consist
