from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="PassengerEngineRailcarConsist",
        id="zeus",
        base_numeric_id=25830,
        name="Zeus",
        subrole="pax_railcar",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 620,
        },
        pantograph_type="z-shaped-single-with-base",
        easter_egg_haulage_speed_bonus=True,
        gen=6,
        sprites_complete=True,
        intro_year_offset=-3,
    )  # introduce early by design

    consist_factory.add_unit(
        class_name="ElectricRailcarPaxUnit",
        weight=39,
        chassis="railcar_32px",
        tail_light="railcar_32px_2",
    )

    consist_factory.add_description("""Gets you from A to Z and back.""")
    consist_factory.add_foamer_facts("""BR Class 365 <i>Networker Express</i>""")

    return consist_factory
