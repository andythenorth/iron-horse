from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='avenger',
                            base_numeric_id=4860,
                            name='Avenger',
                            role='heavy_express',
                            role_child_branch_num=4,
                            power=5800,
                            random_reverse=True,
                            gen=5,
                            pantograph_type='z-shaped-single',
                            intro_date_offset=-2, # introduce slightly earlier than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=100,
                     vehicle_length=8,
                     spriterow_num=0)

    consist.description = """Daft as a brush if you ask me.  Or mad as a badger.  Goes like stink off a shovel though."""
    consist.cite = """Mr. Train"""
    consist.foamer_facts = """BR Class 89."""

    return consist
