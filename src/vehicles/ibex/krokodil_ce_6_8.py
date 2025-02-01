from train import EngineConsist


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="krokodil_ce_6_8",
        base_numeric_id=32710,
        name="SBB Ce 6/8 ii Krokodil",
        subrole="super_heavy_freight",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 2800,
        },
        gen=2,
        pantograph_type="diamond-double",
        # intro_year_offset=-13,  # introduce earlier than gen epoch by design
        sprites_complete=False,
    )

    # 63ft IRL is 8/8, surprisingly short
    consist.add_unit(
        class_name="ElectricEngineUnit", weight=75, vehicle_length=8, spriterow_num=0
    )

    consist.description = """ """
    consist.foamer_facts = """SBB Ce 6/8 ii <i>Krokodil</i>"""

    return consist
