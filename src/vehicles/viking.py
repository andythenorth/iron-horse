from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="viking",
        base_numeric_id=780,
        name="Viking",
        role="freight",
        role_child_branch_num=-1,  # does not directly follow from Merlion
        power=1950,
        random_reverse=True,
        gen=5,
        intro_date_offset=6,  # introduce later than gen epoch by design
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=95, vehicle_length=8, spriterow_num=0
    )

    consist.description = """These came in by boat. Nice size, no trouble to run. Steelworks seem to like em."""
    consist.foamer_facts = (
        """MaK / Vossloh G1206/G1700), Corus Di8, Eurotunnel Class 0001 (Class 21)"""
    )

    return consist
