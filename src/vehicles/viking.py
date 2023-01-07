from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="viking",
        base_numeric_id=9820,
        name="Viking",
        role="freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1950,
        },
        random_reverse=True,
        gen=5,
        intro_year_offset=6,  # introduce later than gen epoch by design
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=95, vehicle_length=8, spriterow_num=0
    )

    consist.description = """These came in by boat. Nice size, no trouble to run. Steelworks seem to like em."""
    consist.foamer_facts = (
        """MaK / Vossloh G1206/G1700), Corus Di8, Eurotunnel Class 0001 (Class 21)"""
    )

    return consist
