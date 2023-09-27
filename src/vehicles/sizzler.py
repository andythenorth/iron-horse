from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="sizzler",
        base_numeric_id=12190,
        name="Sizzler",
        role="ultra_heavy_express",
        role_child_branch_num=4,
        power_by_power_source={
            "AC": 7200,
        },
        random_reverse=True,
        gen=6,
        intro_year_offset=2,  # introduce later than gen epoch by design
        extended_vehicle_life=True,
        pantograph_type="z-shaped-double",
        additional_liveries=["BANGER_BLUE"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=82, vehicle_length=8, spriterow_num=0
    )

    consist.description = """Looks like a cheese to me, goes alright though."""
    consist.foamer_facts = """proposed Bombardier Traxx P200, various electric locomotives from Stadler, Siemens, Adtranz"""

    return consist
