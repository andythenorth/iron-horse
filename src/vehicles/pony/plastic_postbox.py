from train import MailEngineRailcarConsist, DieselRailcarMailUnit


def main(roster_id, **kwargs):
    consist = MailEngineRailcarConsist(
        roster_id=roster_id,
        id="plastic_postbox",
        base_numeric_id=21420,
        name="Plastic Postbox",
        role="mail_railcar",
        subrole_child_branch_num=2,
        replacement_consist_id="pylon",  # consolidates to electro-diesel with Pylon
        power_by_power_source={
            "DIESEL": 560,
        },
        gen=5,
        sprites_complete=True,
        intro_year_offset=-5,
    )  # introduce early by design

    consist.add_unit(
        type=DieselRailcarMailUnit,
        weight=37,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
    )

    consist.description = """The most modern way to move mail and other parcels."""
    consist.foamer_facts = (
        """BR Class 128/130, BR Class 153/155/156/158 <i>Sprinters</i>"""
    )

    return consist
