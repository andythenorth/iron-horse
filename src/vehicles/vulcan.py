from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='vulcan',
                            base_numeric_id=4930,
                            name='Vulcan',
                            role='heavy_express',
                            role_child_branch_num=-2,
                            replacement_consist_id='onslaught', # this Joker ends with Onslaught
                            power=2750,
                            random_reverse=True,
                            gen=4,
                            intro_date_offset=1,  # introduce later than gen epoch by design
                            fixed_run_cost_points=200, # give a serious malus to this one (balancing eh?)
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=105,
                     vehicle_length=8,
                     effect_offsets=[(-1, 0), (1, 0)], # double the smoke eh?
                     spriterow_num=0)

    return consist
