from train import ConsistFactory

# only one autocoach, as autoreplace cannot handle mixed cargo articulated consists
# this means that gen 3 engines will be speed-limited by this unit
# but speed still compares favourably with equivalent era railcars, and there's a capacity bonus also


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="AutoCoachCombineConsist",
        id="auto_coach_pony_gen_2",
        base_numeric_id=4690,
        name="Autocoach Set",
        replacement_consist_id="clipper",  # auto-coach ends with gen 4 clipper
        gen=2,
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="AutoCoachCombineUnitMail",
        weight=16,  # capacity bonus vs similar era non-articulated vehicles
        chassis="empty_20px",
        tail_light="railcar_20px_4",
    )

    consist_factory.add_unit(
        class_name="AutoCoachCombineUnitPax",
        weight=16,  # capacity bonus vs similar era non-articulated vehicles
        chassis="empty_20px",
        tail_light="railcar_20px_4",
    )

    consist_factory.add_description(
        """A coach that you can drive the engine from?  Eee, it's magic."""
    )
    consist_factory.add_foamer_facts(
        """SR and LMS autocoach sets, LNER articulated coach sets"""
    )

    return consist_factory
