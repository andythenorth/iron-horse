from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="PassengerEngineRailcarConsist",
        roster_id=roster_id,
        id="happy_train",
        base_numeric_id=20330,
        name="Happy Train",
        subrole="pax_railcar",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 500,
        },
        gen=6,
        # introduce early by design
        intro_year_offset=-5,
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselRailcarPaxUnit",
        weight=40,
        chassis="railcar_32px",
        tail_light="railcar_32px_2",
    )

    consist_factory.description = (
        """Fast quiet trains for a new era. No more life-expired Tin Rockets."""
    )
    consist_factory.foamer_facts = """Siemens <i>Desiro</i>"""

    return consist_factory
