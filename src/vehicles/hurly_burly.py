from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='hurly_burly',
                            base_numeric_id=390,
                            name='Hurly Burly',
                            role='heavy_express',
                            role_child_branch_num=3,
                            power=1800,
                            tractive_effort_coefficient=0.25,
                            random_reverse=True,
                            gen=2,
                            pantograph_type='diamond-double',
                            intro_date_offset=5,  # introduce later than gen epoch by design
                            fixed_run_cost_points=180, # substantial cost bonus for balance against same-era steam engines
                            sprites_complete=True)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=90,
                     vehicle_length=8,
                     spriterow_num=0)

    consist.description = """By eck, it's a big electric.  Better put some pennies in the meter."""
    consist.cite = """Mr. Train"""
    consist.foamer_facts = """NER Class EE1."""

    return consist
