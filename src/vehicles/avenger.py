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
                            sprites_complete=False)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=100,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
