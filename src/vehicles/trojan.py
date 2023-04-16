from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="trojan",
        base_numeric_id=12010,
        name="Trojan",
        role="freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1700,
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=6,  # introduce later than gen epoch by design
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=95, vehicle_length=8, spriterow_num=0
    )

    consist.description = """Steel yourself, this one's on the move."""
    consist.foamer_facts = """GEC Stephenson steel mill locomotives, Alco RSD-1 export switcher"""

    return consist
