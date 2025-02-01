from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="MailEngineCabbageDVTConsist",
        roster_id=roster_id,
        id="driving_cab_high_speed_mail_pony_gen_6",
        base_numeric_id=17320,
        name="High Speed Driving Van Trailer",
        subrole_child_branch_num=-3,  # driving cab cars are probably jokers?
        gen=6,
        lgv_capable=True,
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="CabbageDVTUnit", weight=34, chassis="railcar_32px"
    )

    consist_factory.description = """Front or back of a train, up to you. Supplies hotel power for the coaches, so your main loco has more power for traction. Seems to work, so here's a new version."""
    consist_factory.foamer_facts = (
        """CAF MK5A Driving Van Trailer (DVT) with added generator"""
    )

    return consist_factory
