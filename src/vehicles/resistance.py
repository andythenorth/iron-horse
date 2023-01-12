from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="resistance",
        base_numeric_id=8850,
        name="Resistance",
        role="ultra_heavy_freight",
        role_child_branch_num=2,
        power_by_power_source={
            "AC": 5800,
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.4,
        random_reverse=True,
        gen=5,
        intro_year_offset=-4, # earlier than the IRL introduction of this never-built train...
        pantograph_type="z-shaped-double",
        caboose_family="railfreight_2",
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=120, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """"""
    )
    consist.foamer_facts = """Proposed BR Class 88, derived from class 58 design"""

    return consist
