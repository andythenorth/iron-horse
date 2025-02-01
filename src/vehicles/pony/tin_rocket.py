from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="PassengerEngineRailcarConsist",
        id="tin_rocket",
        base_numeric_id=21160,
        name="Tin Rocket",
        subrole="pax_railcar",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 400,
        },
        gen=5,
        sprites_complete=True,
        # introduce early by design
        intro_year_offset=-5,
    )

    consist_factory.add_unit(
        class_name="DieselRailcarPaxUnit",
        weight=40,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
    )

    consist_factory.description = (
        """Fast quiet trains for a new era. No more rattling Slammers."""
    )
    consist_factory.foamer_facts = """BR Class 153/155/156/158 <i>Sprinters</i>"""

    return consist_factory
