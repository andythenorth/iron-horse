from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='chinook',
                            base_numeric_id=120,
                            name='Chinook',
                            role='heavy_freight',
                            role_child_branch_num=1,
                            power=2900,
                            gen=4,
                            cc_liveries=['COLOUR_GREY'],
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=80,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.add_unit(type=DieselEngineUnit,
                     weight=80,
                     vehicle_length=6,
                     spriterow_num=1)

    return consist
