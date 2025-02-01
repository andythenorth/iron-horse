from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="PassengerEngineRailcarConsist",
        id="slammer",
        base_numeric_id=21080,
        name="Slammer",
        subrole="pax_railcar",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 300,
        },
        gen=4,
        # introduce early by design
        intro_year_offset=-5,
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselRailcarPaxUnit",
        weight=37,
        chassis="railcar_32px",
        tail_light="railcar_32px_2",
    )

    consist_factory.add_description(
        """Fast quiet trains for a new era. No more lurching Deasils."""
    )
    consist_factory.add_foamer_facts("""BR Class 108/117/121 and similar units""")

    result.append(consist_factory)

    return result
