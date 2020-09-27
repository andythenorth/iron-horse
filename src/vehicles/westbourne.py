from train import PassengerEngineMetroConsist, MetroUnit


def main(roster_id):
    consist = PassengerEngineMetroConsist(roster_id=roster_id,
                                          id='westbourne',
                                          base_numeric_id=360,
                                          name='Westbourne',
                                          role='pax_metro',
                                          role_child_branch_num=1,
                                          power=900,
                                          gen=2,
                                          sprites_complete=True)

    consist.add_unit(type=MetroUnit,
                     weight=36,
                     capacity=160,
                     chassis='railcar_32px',
                     tail_light='metro_32px_1',
                     repeat=2)

    consist.description = """"""
    consist.foamer_facts = """London Underground 1938/1949 Stock."""

    return consist
