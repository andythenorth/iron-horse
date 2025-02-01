from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="PassengerEngineRailbusConsist",
        id="skipper",
        base_numeric_id=240,
        name="Skipper",
        subrole="pax_railbus",
        subrole_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={
            "DIESEL": 400,
        },
        gen=5,
        # introduce early by design
        intro_year_offset=-4,
        pax_car_capacity_type="railbus_combine",  # specific to combined mail + pax consist_factory
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselRailcarCombineUnitMail",
        weight=20,
        chassis="railbus_lwb_20px",
        tail_light="railcar_20px_1",
    )

    consist_factory.add_unit(
        class_name="DieselRailcarCombineUnitPax",
        weight=20,
        chassis="railbus_lwb_20px",
        tail_light="railcar_20px_2",
    )

    consist_factory.add_description("""Patience is the virtue of the donkeys.""")
    consist_factory.add_foamer_facts("""BR Class 141/142/143/144 <i>Pacers</i>""")

    return consist_factory
