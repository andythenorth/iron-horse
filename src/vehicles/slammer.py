from train import PassengerEngineRailcarConsist, DieselRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineRailcarConsist(roster_id=roster_id,
                                            id='slammer',
                                            base_numeric_id=470,
                                            name='Slammer',
                                            role='pax_railcar',
                                            role_child_branch_num=1,
                                            power=300,
                                            gen=4,
                                            sprites_complete=True,
                                            intro_date_offset=-5)  # introduce early by design

    consist.add_unit(type=DieselRailcarPaxUnit,
                     weight=37,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_2')

    return consist
