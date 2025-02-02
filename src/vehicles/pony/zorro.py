from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="MailEngineRailcarConsist",
        id="zorro",
        base_numeric_id=21030,
        name="Zorro",
        subrole="mail_railcar",
        subrole_child_branch_num=1,
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 420,
        },
        gen=3,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="DieselRailcarMailUnit",
        weight=18,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        chassis="railcar_ng_24px",
        tail_light="railcar_24px_1",
    )

    consist_factory.define_description(
        """A reliable way to move mail, supplies and express freight. Goats are not however, at this time, permitted."""
    )
    consist_factory.define_foamer_facts("""CFC Autorail Billard, CFC X2000/X5000""")

    result.append(consist_factory)

    return result
