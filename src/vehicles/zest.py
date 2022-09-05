from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="zest",
        base_numeric_id=14510,
        name="Zest",
        role="branch_freight",
        role_child_branch_num=2,
        power_by_power_source={
            "AC": 1600,
        },
        random_reverse=True,
        pantograph_type="diamond-single",
        gen=4,
        intro_year_offset=6,  # introduce later than gen epoch by design
        vehicle_life=70,  # extended vehicle life to match Stoat
        fixed_run_cost_points=105,  # substantial cost bonus so it can make money
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=54, vehicle_length=6, spriterow_num=0
    )

    consist.description = """Solid unit."""
    consist.foamer_facts = """NER ES1, Metropolitan Railway camel-back and box-cab locomotives, Westoe Colliery electrics, generic steeple-cab locomotives"""

    return consist
