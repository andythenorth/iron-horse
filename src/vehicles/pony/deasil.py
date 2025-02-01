from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="PassengerEngineRailcarConsist",
        id="deasil",
        base_numeric_id=21240,
        name="Deasil",
        subrole="pax_railcar",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 200,
        },
        gen=3,
        sprites_complete=True,
        intro_year_offset=-5,
    )  # introduce early by design

    consist_factory.add_unit(
        class_name="DieselRailcarPaxUnit",
        weight=30,
        chassis="railcar_32px",
        tail_light="railcar_32px_1",
    )

    consist_factory.add_description(
        """Fast quiet trains for a new era. No more noisy steam engines."""
    )
    consist_factory.add_foamer_facts("""LNER / Armstrong-Whitworth Railcars""")

    return consist_factory
