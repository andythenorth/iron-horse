from train import MailEngineCargoSprinterCabEngineConsist, DieselRailcarMailUnit


def main(roster_id):
    consist = MailEngineCargoSprinterCabEngineConsist(roster_id=roster_id,
                                                      id='cargo_sprinter_cab',
                                                      base_numeric_id=3000,
                                                      name='Cargo Sprinter',
                                                      role='mail_railcar',  # abuse of existing railcar role for convenience
                                                      role_child_branch_num=-1,
                                                      power=1400,
                                                      dual_headed=True,
                                                      gen=6,
                                                      intro_date_offset=-3,  # introduce earlier than gen epoch by design
                                                      sprites_complete=True)

    consist.add_unit(type=DieselRailcarMailUnit,
                     weight=76,
                     # no pax capacity on Helm Wind cabs
                     capacity=0,
                     spriterow_num=0,
                     chassis='4_axle_solid_express_32px',
                     tail_light='very_high_speed_32px_1')

    consist.description = """"""
    consist.foamer_facts = """"""

    return consist
