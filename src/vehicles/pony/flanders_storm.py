from train import EngineConsist, ElectricEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="flanders_storm",
        base_numeric_id=25150,
        name="Flanders Storm",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 6200,
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.4,
        random_reverse=True,
        gen=5,
        pantograph_type="z-shaped-double",
        intro_year_offset=5,  # introduce later than gen epoch by design
        caboose_family="railfreight_2",
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["RAILFREIGHT_TRIPLE_GREY", "DB_SCHENKER"],
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
