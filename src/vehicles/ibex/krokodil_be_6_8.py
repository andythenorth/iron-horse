from train import EngineConsist, ElectricEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="krokodil_be_6_8",
        base_numeric_id=32850,
        name="SBB Be 6/8 ii Krokodil",
        role="super_heavy_freight",
        role_child_branch_num=2,
        power_by_power_source={
            "AC": 3700,
        },
        gen=3,
        pantograph_type="diamond-double",
        # intro_year_offset=-13,  # introduce earlier than gen epoch by design
        sprites_complete=False,
    )

    # 63ft IRL is 8/8, surprisingly short
    consist.add_unit(
        type=ElectricEngineUnit, weight=75, vehicle_length=8, spriterow_num=0
    )

    consist.description = """ """
    consist.foamer_facts = """SBB Be 6/8 ii <i>Krokodil</i>"""

    return consist
