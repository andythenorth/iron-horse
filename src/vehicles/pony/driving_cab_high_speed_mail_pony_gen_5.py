from train import MailEngineCabbageDVTConsist, CabbageDVTUnit


def main(roster_id, **kwargs):
    consist = MailEngineCabbageDVTConsist(
        roster_id=roster_id,
        id="driving_cab_high_speed_mail_pony_gen_5",
        base_numeric_id=18090,
        name="High Speed Driving Van Trailer",
        role_child_branch_num=-2,  # driving cab cars are probably jokers?
        gen=5,
        lgv_capable=True,  # for lolz
        sprites_complete=True,  # !! needs gen 6 pax liveries - add later
    )

    consist.add_unit(type=CabbageDVTUnit, weight=32, chassis="railcar_32px")

    consist.description = """Front or back of a train, up to you. Supplies hotel power for the coaches, so your main loco has more power for traction. Clever idea we had eh?"""
    consist.foamer_facts = """BR MK3 Driving Van Trailer (DVT) with added generator"""

    return consist
