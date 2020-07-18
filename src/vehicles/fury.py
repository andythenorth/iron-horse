from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='fury',
                            base_numeric_id=2180,
                            name='Fury',
                            role='heavy_express',
                            role_child_branch_num=2,
                            power=4000,
                            random_reverse=True,
                            gen=5,
                            replacement_consist_id='revolution', # this line ends with Fury and is merged to heavy_express 3
                            pantograph_type='z-shaped-double',
                            intro_date_offset=1,  # introduce later than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=82,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
