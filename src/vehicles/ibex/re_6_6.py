from train import EngineConsist


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="re_6_6",
        base_numeric_id=40,
        name="SBB Re 6/6",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=3,
        power_by_power_source={
            "AC": 9900,
        },
        gen=4,
        # pantograph_type="diamond-double",
        # intro_year_offset=-13,  # introduce earlier than gen epoch by design
        sprites_complete=False,
    )

    # !! Re 6/6 is only 63ft IRL, so 8/8, but that's weird because 10k HP in 8/8 is weird, so lengthen and articulate
    consist.add_unit(
        class_name="ElectricEngineUnit", weight=75, vehicle_length=5, spriterow_num=0
    )
    consist.add_unit(
        class_name="ElectricEngineUnit", weight=75, vehicle_length=5, spriterow_num=1
    )

    consist.description = """ """
    consist.foamer_facts = """SBB Re 6/6"""

    return consist
