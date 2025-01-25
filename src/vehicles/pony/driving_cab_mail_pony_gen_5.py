from train import MailEngineCabbageDVTConsist, CabbageDVTUnit


def main(roster_id, **kwargs):
    consist = MailEngineCabbageDVTConsist(
        roster_id=roster_id,
        id="driving_cab_mail_pony_gen_5",
        base_numeric_id=19970,
        name="Driving Van Trailer",
        subrole_child_branch_num=-1,  # driving cab cars are probably jokers?
        gen=5,
        liveries="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    consist.add_unit(type=CabbageDVTUnit, weight=32, chassis="railcar_32px")

    consist.description = """Front or back of a train, up to you. Supplies hotel power for the coaches, so your main loco has more power for traction. Clever idea we had eh?"""
    consist.foamer_facts = (
        """BR parcels Propelling Control Vehicle (PCV) with added generator"""
    )

    return consist
