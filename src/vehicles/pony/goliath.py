from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="goliath",
        base_numeric_id=21230,
        name="Goliath",
        subrole="branch_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1650,
        },
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        random_reverse=True,
        gen=5,
        intro_year_offset=2,  # introduce later than gen epoch by design
        caboose_family="railfreight_2",
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit", weight=71, vehicle_length=6, spriterow_num=0
    )

    consist_factory.description = """It gets the job done either way."""
    consist_factory.foamer_facts = """YEC <i>Janus</i>, Corus <i>Trojan</i>"""

    return consist_factory
