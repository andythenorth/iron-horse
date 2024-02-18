from train import EngineConsist, SteamEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="celt",
        base_numeric_id=11360,
        name="2-8-4 Celt",
        role="freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 1500,
        },
        tractive_effort_coefficient=0.24,
        gen=3,
        # note that livery names are metadata only and can repeat for different spriterows
        # additional_liveries=["FREIGHT_BLACK"],
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=90, vehicle_length=8, spriterow_num=0)

    consist.description = (
        """Celt, boyo, she's like a choir in the valleys - powerful, resonant, hefty."""
    )
    consist.foamer_facts = """GWR 7200 Class, LNER Class S1, LNER Class T1"""

    return consist
