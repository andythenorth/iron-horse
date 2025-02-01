from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="PassengerEngineRailbusConsist",
        id="zipper",
        base_numeric_id=260,
        name="Zipper",
        subrole="pax_railbus",
        subrole_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={
            "DIESEL": 480,
        },
        gen=6,
        # introduce early by design
        intro_year_offset=-4,
        pax_car_capacity_type="railbus_combine",  # specific to combined mail + pax consist_factory
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselRailcarCombineUnitMail",
        weight=21,
        chassis="railbus_lwb_20px",
        tail_light="railcar_20px_1",
    )

    consist_factory.add_unit(
        class_name="DieselRailcarCombineUnitPax",
        weight=21,
        chassis="railbus_lwb_20px",
        tail_light="railcar_20px_1",
    )

    consist_factory.description = """It's the same donkey, but with a new saddle."""
    consist_factory.foamer_facts = """BR Class 144e <i>Pacer</i>, Vivarail D-Train"""

    return consist_factory
