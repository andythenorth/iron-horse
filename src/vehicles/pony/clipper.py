from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="PassengerEngineRailbusConsist",
        id="clipper",
        base_numeric_id=250,
        name="Clipper",
        subrole="pax_railbus",
        subrole_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={
            "DIESEL": 300,
        },
        gen=4,
        # introduce early by design
        intro_year_offset=-4,
        pax_car_capacity_type="railbus_combine",  # specific to combined mail + pax consist_factory
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselRailcarCombineUnitMail",
        weight=18,
        chassis="railbus_swb_20px",
        tail_light="railcar_20px_1",
    )

    consist_factory.add_unit(
        class_name="DieselRailcarCombineUnitPax",
        weight=18,
        chassis="railbus_swb_20px",
        tail_light="railcar_20px_1",
    )

    consist_factory.add_description(
        """The horses of hope gallop, but the donkeys of experience go slowly."""
    )
    consist_factory.add_foamer_facts(
        """BR 1st generation AC Cars/Wickham/Waggon-und Maschinenbau and similar railbuses"""
    )

    return consist_factory
