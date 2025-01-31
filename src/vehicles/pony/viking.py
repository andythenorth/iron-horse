from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="viking",
        base_numeric_id=21140,
        name="Viking",
        subrole="freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 2200,
        },
        random_reverse=True,
        gen=5,
        intro_year_offset=6,  # introduce later than gen epoch by design
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit", weight=95, vehicle_length=8, spriterow_num=0
    )

    consist_factory.description = """These came in by boat. Nice size, no trouble to run. Steelworks seem to like em."""
    consist_factory.foamer_facts = (
        """MaK / Vossloh G1206/G1700), Corus Di8, Eurotunnel Class 0001 (Class 21)"""
    )

    return consist_factory
