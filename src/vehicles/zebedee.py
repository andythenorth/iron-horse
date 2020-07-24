from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='zebedee',
                            base_numeric_id=4950,
                            name='Zebedee',
                            role='heavy_express',
                            role_child_branch_num=-3,
                            power=3820,
                            random_reverse=True,
                            gen=4,
                            pantograph_type='z-shaped-double',
                            intro_date_offset=10,  # introduce much later than gen epoch by design
                            sprites_complete=False)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=80,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
