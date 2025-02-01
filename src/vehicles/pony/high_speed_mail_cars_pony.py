from train import ConsistFactory


def main(roster_id, **kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="MailHighSpeedCarConsist",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30690,
        gen=5,
        subtype="U",
        liveries="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="ExpressMailCar", chassis="high_speed_32px")

    result.append(consist_factory)

    return result
