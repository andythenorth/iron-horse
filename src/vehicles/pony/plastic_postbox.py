from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="MailEngineRailcarConsist",
        roster_id=roster_id,
        id="plastic_postbox",
        base_numeric_id=21420,
        name="Plastic Postbox",
        subrole="mail_railcar",
        subrole_child_branch_num=2,
        replacement_consist_id="pylon",  # consolidates to electro-diesel with Pylon
        power_by_power_source={
            "DIESEL": 560,
        },
        gen=5,
        sprites_complete=True,
        intro_year_offset=-5,
    )  # introduce early by design

    consist_factory.add_unit(
        class_name="DieselRailcarMailUnit",
        weight=37,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
    )

    consist_factory.description = """The most modern way to move mail and other parcels."""
    consist_factory.foamer_facts = (
        """BR Class 128/130, BR Class 153/155/156/158 <i>Sprinters</i>"""
    )

    return consist_factory
