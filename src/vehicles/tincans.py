from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="tincans",
        base_numeric_id=370,
        name="Tincans",
        role="ultra_heavy_freight",
        role_child_branch_num=-2,
        power_by_power_source={
            "AC": 6200, # match to Resistance
        },
        # dibble for game balance, assume some slip control
        tractive_effort_coefficient=0.34,
        gen=5,
        pantograph_type="z-shaped-single",
        intro_year_offset=-13,  # introduce earlier than gen epoch by design
        additional_liveries=[],
        sprites_complete=True,
        sprites_additional_liveries_needed=True, # railfreight?
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=70, vehicle_length=6, spriterow_num=0, repeat=2
    )

    consist.description = (
        """“I would not wish any companion in the world but you.”"""
    )
    consist.foamer_facts = """Polish PKP EU07 (derived from UK class 83 design)"""

    return consist
