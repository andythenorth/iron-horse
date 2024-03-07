from train import EngineConsist, SteamEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="celt",
        base_numeric_id=31010,
        name="2-8-4 Celt",
        role="freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 1500,
        },
        tractive_effort_coefficient=0.24,
        random_reverse=True,
        gen=3,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    consist.add_unit(type=SteamEngineUnit, weight=90, vehicle_length=8, spriterow_num=0)

    consist.description = (
        """Celt, boyo, she's like a choir in the valleys - powerful, resonant, hefty."""
    )
    consist.foamer_facts = """'Austerity' locomotives, Indian Railways WT Class"""

    return consist
