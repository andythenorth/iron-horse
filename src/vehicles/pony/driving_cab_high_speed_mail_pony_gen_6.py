from train import MailEngineCabbageDVTConsist, CabbageDVTUnit


def main(roster_id):
    consist = MailEngineCabbageDVTConsist(
        roster_id=roster_id,
        id="driving_cab_high_speed_mail_pony_gen_6",
        base_numeric_id=13030,
        name="High Speed Driving Van Trailer",
        role_child_branch_num=-3,  # driving cab cars are probably jokers?
        gen=6,
        lgv_capable=True,
        sprites_complete=True,
    )

    consist.add_unit(type=CabbageDVTUnit, weight=34, chassis="railcar_32px")

    consist.description = """Front or back of a train, up to you. Supplies hotel power for the coaches, so your main loco has more power for traction. Seems to work, so here's a new version."""
    consist.foamer_facts = """CAF MK5A Driving Van Trailer (DVT) with added generator"""

    return consist
