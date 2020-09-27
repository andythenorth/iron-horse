from train import PassengerEngineRailcarConsist, DieselRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineRailcarConsist(roster_id=roster_id,
                                            id='mumble',
                                            base_numeric_id=140,
                                            name='Mumble',
                                            role='pax_railcar',
                                            role_child_branch_num=1,
                                            base_track_type='NG',
                                            power=250,
                                            gen=3,
                                            sprites_complete=True)

    consist.add_unit(type=DieselRailcarPaxUnit,
                     weight=18,
                     effect_z_offset=11, # reduce smoke z position to suit NG engine height
                     chassis='railcar_ng_24px',
                     tail_light='railcar_24px_1')

    consist.description = """"""
    consist.cite = """Roberto Flange"""
    consist.foamer_facts = """CFC Autorail Billard, CFC X2000/X5000."""

    return consist
