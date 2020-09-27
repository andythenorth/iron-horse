from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='pikel',
                            base_numeric_id=430,
                            name='Pikel',
                            role='universal',
                            role_child_branch_num=1,
                            power=650,
                            random_reverse=True,
                            base_track_type='NG',
                            gen=3,
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=26,
                     vehicle_length=4,
                     effect_z_offset=9, # reduce smoke z position to suit NG engine height
                     spriterow_num=0)

    consist.description = """"""
    consist.cite = """Roberto Flange"""
    consist.foamer_facts = """FAUR L45H B-B, generic narrow-gauge diesel locomotives."""

    return consist
