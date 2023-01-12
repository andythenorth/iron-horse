from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="sizzler",
        base_numeric_id=12190,
        name="Sizzler",
        role="ultra_heavy_express",
        role_child_branch_num=2,
        power_by_power_source={
            "AC": 6800,  # roughly brackets Quietus
        },
        random_reverse=True,
        gen=6,
        pantograph_type="z-shaped-double",
        intro_year_offset=2,  # introduce later than gen epoch by design
        # banger blue?
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=82, vehicle_length=8, spriterow_num=0
    )

    consist.description = """Looks like a cheese to me, goes alright though."""
    consist.foamer_facts = """proposed Bombardier Traxx P200, various electric locomotives from Stadler, Siemens, Adtranz"""

    return consist
