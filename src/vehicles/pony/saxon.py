from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="saxon",
        base_numeric_id=21250,
        name="0-8-0 Saxon",
        subrole="branch_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 1000,
        },
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        random_reverse=True,
        gen=3,
        intro_year_offset=-8,  # introduce earlier than gen epoch by design
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "FREIGHT_BLACK", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="SteamEngineUnit", weight=65, vehicle_length=6, spriterow_num=0
    )

    consist_factory.add_description(
        """I didn't do these, we've shipped them in. On ships like. On the sea. They pull well mind you."""
    )
    consist_factory.add_foamer_facts("""SR Z class, SR USA class (USATC S100 Class)""")

    result.append(consist_factory)

    return result
