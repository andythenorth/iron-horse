from train import PassengerEngineRailcarConsist, DieselRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineRailcarConsist(roster_id=roster_id,
                                            id='tin_rocket',
                                            base_numeric_id=530,
                                            name='Tin Rocket',
                                            role='pax_railcar',
                                            role_child_branch_num=1,
                                            power=400,
                                            gen=5,
                                            sprites_complete=True,
                                            intro_date_offset=-5)  # introduce early by design

    consist.add_unit(type=DieselRailcarPaxUnit,
                     weight=40,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_3')

    consist.description = """"""
    consist.foamer_facts = """BR Class 153/155/156/158 <i>Sprinters</i>."""

    return consist
