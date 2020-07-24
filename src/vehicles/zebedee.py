from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='zebedee',
                            base_numeric_id=4950,
                            name='Zebedee',
                            role='heavy_express',
                            role_child_branch_num=-3, # it's a joker, tried it as heavy express 4, the power progression and dates are all wrong for that
                            power=4000, # bit unsure about power on this one, a larger electric is wanted, but don't want to power creep gen 4 too much
                            random_reverse=True,
                            gen=4,
                            pantograph_type='z-shaped-double',
                            intro_date_offset=9,  # introduce much later than gen epoch by design
                            sprites_complete=False)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=82,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
