from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='pinhorse',
                            base_numeric_id=3250,
                            name='Pinhorse',
                            role='branch_express',
                            role_child_branch_num=2,
                            power=1100,
                            random_reverse=True,
                            pantograph_type='diamond-single',
                            gen=3,
                            intro_date_offset=5, # introduce later than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=60,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.description = """Mr. Bulleid and Mr. Raworth drew these up for me. For small jobs, you won't go far wrong with em."""
    consist.cite = """Mr. Train"""

    return consist
