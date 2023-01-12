from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="tincans",
        base_numeric_id=370,
        name="Tincans",
        role="ultra_heavy_freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "AC": 5200,
        },
        # dibble for game balance, assume some slip control
        tractive_effort_coefficient=0.34,
        gen=5,
        pantograph_type="z-shaped-single",
        intro_year_offset=-13,  # introduce earlier than gen epoch by design
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=70, vehicle_length=6, spriterow_num=0, repeat=2
    )

    consist.description = (
        """"""
    )
    consist.foamer_facts = """"""

    return consist
