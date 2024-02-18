from train import EngineConsist, ElectricEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="sbb_fb_4_4",
        base_numeric_id=13870,
        name="SBB Sb 4/4",
        role="branch_express",
        role_child_branch_num=2,
        power_by_power_source={
            # "AC": 1700,
            "AC": 10,
        },
        gen=2,
        pantograph_type="diamond-double",
        intro_year_offset=-5,  # introduce earlier than gen epoch by design
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=75, vehicle_length=6, spriterow_num=0
    )

    consist.description = """ """
    consist.foamer_facts = """SBB Fb 4/4"""

    return consist
