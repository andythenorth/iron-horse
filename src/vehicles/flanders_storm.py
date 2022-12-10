from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="flanders_storm",
        base_numeric_id=10780,
        name="Flanders Storm",
        role="ultra_heavy_freight",
        role_child_branch_num=1,
        power_by_power_source={
            "AC": 5800,  # big jump from previous, IRL matches class 89 not 92
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.4,
        random_reverse=True,
        gen=5,
        pantograph_type="z-shaped-double",
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        caboose_family="railfreight_2",
        alternative_liveries=["RAILFREIGHT_TRIPLE_GREY"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=120, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """This is a right proper engine.  Does work enough for two."""
    )
    consist.foamer_facts = """BR Class 92"""

    return consist
