from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='sizzler',
                            base_numeric_id=3150,
                            name='Sizzler',
                            role='heavy_express',
                            role_child_branch_num=4,
                            power=6600, # match to same gen HST
                            random_reverse=True,
                            gen=6,
                            pantograph_type='z-shaped-double',
                            intro_date_offset=2,  # introduce later than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=82,
                     vehicle_length=8,
                     spriterow_num=0)

    consist.description = """Looks like a cheese to me, goes alright though."""
    consist.cite = """Mr. Train"""
    consist.foamer_facts = """proposed Bombardier Traxx P200, various electric locomotives from Stadler, Siemens, Adtranz."""

    return consist
