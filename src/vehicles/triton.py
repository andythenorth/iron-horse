from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='triton',
                            base_numeric_id=3910,
                            name='Triton',
                            role='heavy_freight',
                            role_child_branch_num=3,
                            power=6850, # relatively tiny jump from gen 5, compared to gen 4->5, very high-powered single unit engines are unbalanced for Pony
                            # dibble for game balance, assume super-slip control
                            tractive_effort_coefficient=0.4,
                            random_reverse=True,
                            gen=6,
                            pantograph_type='z-shaped-double',
                            intro_date_offset=7,  # introduce later than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=128,
                     vehicle_length=8,
                     spriterow_num=0)

    consist.description = """Nice humming noise these make.  What else can I tell you?  Lot of power, you won't need many of these to the gallon."""
    consist.foamer_facts = """BR Class 92, Newag Dragon"""

    return consist
