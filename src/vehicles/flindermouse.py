from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="flindermouse",
        base_numeric_id=790,
        name="Flindermouse",
        role="ultra_heavy_freight",
        role_child_branch_num=1,
        power_by_power_source={
            "AC": 2500,
        },
        speed=60,  # continues a long way into gen 3, so go faster
        gen=2,
        pantograph_type="diamond-double",
        intro_year_offset=7,  # introduce later than gen epoch by design
        additional_liveries=["FREIGHT_BLACK", "BANGER_BLUE"],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=65, vehicle_length=6, spriterow_num=0, repeat=2
    )

    consist.description = """We're giving electrics a go for freight.  Don't right know if they'll catch on, but they can pull, I give em that."""
    consist.foamer_facts = """NER EF1"""

    return consist
