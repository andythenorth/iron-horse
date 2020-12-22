from train import EngineConsist, ElectroDieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="quietus",
        base_numeric_id=5370,
        name="Quietus",
        role="heavy_freight",
        role_child_branch_num=-1,  # child branch 1 empty, for tech tree drawing reasons (blackthorn and quietus in branch -1)
        power=3250,  # HP matched to equivalent gen pure diesels
        power_by_railtype={
            "RAIL": 3250,
            "ELRL": 6700,
        },  # based on the Stadler Eurodual, really quite high values for both diesel and el (also matches Newag Dragon, which the shape is taken from)
        tractive_effort_coefficient=0.375, # assume slip control magic
        random_reverse=True,
        pantograph_type="z-shaped-double",
        gen=6,
        fixed_run_cost_points=500,  # run cost nerf for high power + dual mode
        intro_date_offset=8,  # introduce later than gen epoch by design
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectroDieselEngineUnit, weight=136, vehicle_length=8, spriterow_num=0
    )

    consist.description = """It'll get there and back again, in any weather."""
    consist.foamer_facts = """Stadler Eurodual, Newag Dragon, CAF Bitrac"""

    return consist
