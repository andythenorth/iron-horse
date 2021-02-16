from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="zest",
        base_numeric_id=5470,
        name="Zest",
        role="branch_freight",
        role_child_branch_num=2,
        power=1600,
        random_reverse=True,
        pantograph_type="diamond-single",
        gen=4,
        intro_date_offset=6,  # introduce later than gen epoch by design
        fixed_run_cost_points=105,  # substantial cost bonus so it can make money
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=54, vehicle_length=6, spriterow_num=0
    )

    consist.description = """Nippy little bugger."""
    consist.foamer_facts = """NER ES1, Metropolitan Railway camel-back and box-cab locomotives, generic steeple-cab locomotives"""

    return consist
