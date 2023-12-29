from train import MailEngineCabbageDVTConsist, CabbageDVTUnit


def main(roster_id):
    consist = MailEngineCabbageDVTConsist(
        roster_id=roster_id,
        id="driving_cab_mail_pony_gen_5",
        base_numeric_id=9410,
        name="Driving Van Trailer",
        role_child_branch_num=-1,  # driving cab cars are probably jokers?
        gen=5,
        sprites_complete=False, # needs gen 6 pax liveries, possibly other things
    )

    consist.add_unit(type=CabbageDVTUnit, weight=32, chassis="railcar_32px")

    consist.description = """Front or back of a train, up to you. Supplies hotel power for the coaches, so your main loco has more power for traction. Clever idea we had eh?"""
    consist.foamer_facts = """BR parcels Propelling Control Vehicle (PCV) with added generator"""

    return consist
