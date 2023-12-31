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
            "AC": 6200,  # match to Resistance
        },
        # dibble for game balance, assume some slip control
        tractive_effort_coefficient=0.34,
        gen=5,
        intro_year_offset=-13,  # introduce earlier than gen epoch by design
        extended_vehicle_life=True,
        pantograph_type="z-shaped-single",
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["RAILFREIGHT_RED_STRIPE"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=70, vehicle_length=6, spriterow_num=0, repeat=2
    )

    consist.description = """“I would not wish any companion in the world but you.”"""
    consist.foamer_facts = """Polish PKP EU07 (derived from UK Class 83 design)"""

    return consist
