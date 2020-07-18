from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='boar_cat',
                            base_numeric_id=1320,
                            name='Boar Cat',
                            role='universal',
                            role_child_branch_num=1,
                            power=800,
                            random_reverse=True,
                            base_track_type='NG',
                            gen=4,
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=30,
                     vehicle_length=4,
                     effect_z_offset=9, # reduce smoke z position to suit NG engine height
                     spriterow_num=0)

    return consist
