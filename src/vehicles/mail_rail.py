from train import MailEngineRailcarConsist, DieselRailcarMailUnit


def main(roster_id):
    consist = MailEngineRailcarConsist(roster_id=roster_id,
                                       id='mail_rail',
                                       base_numeric_id=3000,
                                       name='Mail Rail',
                                       role='mail_railcar',
                                       role_child_branch_num=1,
                                       power=700,
                                       gen=6,
                                       sprites_complete=True,
                                       intro_date_offset=-5)  # introduce early by design

    consist.add_unit(type=DieselRailcarMailUnit,
                     weight=37,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_2')

    consist.description = """This is the night mail crossing the border, bringing the cheque and the postal order.""" # WH Auden, The Night Mail
    consist.foamer_facts = """BR Class 128, Class 325."""

    return consist
