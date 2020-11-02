from train import AutoCoachCombineConsist, AutoCoachCombineUnitMail, AutoCoachCombineUnitPax

# only one autocoach, as autoreplace cannot handle mixed cargo articulated consists
# this means that gen 3 engines will be speed-limited by this unit
# but speed still compares favourably with equivalent era railcars, and there's a capacity bonus also

def main(roster_id):
    consist = AutoCoachCombineConsist(
        roster_id=roster_id,
        id="auto_coach_pony_gen_2",
        base_numeric_id=4690,
        name="Autocoach Set",
        replacement_consist_id='slammer', # auto-coach ends with gen 4 Slammer
        gen=2,
        intro_date_offset=15, # introduce significantly later than gen epoch
        sprites_complete=True,
    )

    consist.add_unit(
        type=AutoCoachCombineUnitMail,
        weight=16, # capacity bonus vs similar era non-articulated vehicles
        chassis='empty_20px',
    )

    consist.add_unit(
        type=AutoCoachCombineUnitPax,
        weight=16, # capacity bonus vs similar era non-articulated vehicles
        chassis='empty_20px',
    )

    consist.description = """A coach that you can drive the engine from?  Eee, it's magic."""
    consist.foamer_facts = """SR and LMS autocoach sets, LNER articulated coach sets"""

    return consist
