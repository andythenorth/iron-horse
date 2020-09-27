from train import PassengerEngineMetroConsist, MetroUnit


def main(roster_id):
    consist = PassengerEngineMetroConsist(roster_id=roster_id,
                                          id='fleet',
                                          base_numeric_id=210,
                                          name='Fleet',
                                          role='pax_metro',
                                          role_child_branch_num=1,
                                          power=1100,
                                          gen=3,
                                          sprites_complete=True)

    # should be 4 short units, not 2 long but eh
    consist.add_unit(type=MetroUnit,
                     weight=36,
                     capacity=200,
                     chassis='railcar_32px',
                     tail_light='metro_32px_1',
                     repeat=2)

    consist.description = """"""
    consist.foamer_facts = """London Underground 1996 Stock."""

    return consist
