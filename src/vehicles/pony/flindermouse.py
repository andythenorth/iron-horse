from train import EngineConsist, ElectricEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="flindermouse",
        base_numeric_id=790,
        name="Flindermouse",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 2500,
        },
        speed=60,  # continues a long way into gen 3, so go faster
        gen=2,
        pantograph_type="diamond-double",
        intro_year_offset=7,  # introduce later than gen epoch by design
        extended_vehicle_life=True,
        # additional_liveries=["FREIGHT_BLACK", "BANGER_BLUE"],
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        sprites_complete=True,
        sprites_additional_liveries_potential=True,  # nightshade / nighthawk?
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=65, vehicle_length=6, spriterow_num=0, repeat=2
    )

    consist.description = """We're giving electrics a go for freight.  Don't right know if they'll catch on, but they can pull, I give em that."""
    consist.foamer_facts = """NER EF1"""

    consist.clone(base_numeric_id=34920, clone_units=[1, 0])

    return consist
