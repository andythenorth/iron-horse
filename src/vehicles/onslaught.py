from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='onslaught',
                            base_numeric_id=4290,
                            name='Onslaught',
                            role='heavy_express',
                            role_child_branch_num=2,
                            power=3300,
                            random_reverse=True,
                            gen=5,
                            intro_date_offset=-8, # let's be really early with this one to give a mail engine matching Blaze HST intro date
                            fixed_run_cost_points=400, # give a serious malus to this one (balancing eh?)
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=100,
                     vehicle_length=8,
                     spriterow_num=0)

    consist.description = """ """
    consist.foamer_facts = """BR Class 50, proposed English Electric / BR Class 51 <i>Super Deltic</i>."""

    return consist
