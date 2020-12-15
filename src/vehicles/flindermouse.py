from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='flindermouse',
                            base_numeric_id=790,
                            name='Flindermouse',
                            role='very_heavy_freight',
                            role_child_branch_num=2,
                            power=2500,
                            gen=3,
                            pantograph_type='diamond-double',
                            intro_date_offset=-23,  # introduce earlier than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=65,
                     vehicle_length=6,
                     spriterow_num=0,
                     repeat=2)

    consist.description = """We're giving electrics a go for freight.  Don't right know if they'll catch on, but they can pull, I give em that."""
    consist.foamer_facts = """NER EF1"""

    return consist
