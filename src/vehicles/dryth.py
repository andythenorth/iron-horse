from train import EngineConsist, ElectricEngineUnit

def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="dryth",
        base_numeric_id=4880,
        name="Dryth",
        role="ultra_heavy_freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "AC": 2900,
        },
        speed=75,  # continues a long way into gen 4, so go faster
        gen=3,
        pantograph_type="diamond-single",
        intro_year_offset=8,  # introduce later than gen epoch by design
        additional_liveries=["BANGER_BLUE"],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=70, vehicle_length=6, spriterow_num=0, repeat=2
    )

    consist.description = (
        """"""
    )
    consist.foamer_facts = """"""

    return consist
