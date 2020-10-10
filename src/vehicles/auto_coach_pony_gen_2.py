from train import MailEngineAutoCoachCombineConsist, AutoCoachCombineUnitMail, AutoCoachCombineUnitPax


def main(roster_id):
    consist = MailEngineAutoCoachCombineConsist(
        roster_id=roster_id,
        id="auto_coach_pony_gen_2",
        base_numeric_id=4690,
        name="Auto Coach",
        gen=2,
        sprites_complete=False,
    )

    consist.add_unit(
        type=AutoCoachCombineUnitMail,
        weight=32,
        chassis="jacobs_solid_express_20px",
    )

    consist.add_unit(
        type=AutoCoachCombineUnitPax,
        weight=32,
        chassis="jacobs_solid_express_20px",
    )

    consist.description = """"""
    consist.foamer_facts = """"""

    return consist
