from train import EngineConsist, MetroUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="debden",
        base_numeric_id=24440,
        name="Debden",
        role="metro",
        role_child_branch_num=1,
        power_by_power_source={
            "METRO": 1050,
        },
        random_reverse=True,
        gen=2,
        intro_year_offset=3,  # introduce later than gen epoch by design
        fixed_run_cost_points=120,  # substantial cost bonus for balance against same-era steam engines
        extended_vehicle_life=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        sprites_complete=False,
    )

    consist.add_unit(
        type=MetroUnit, weight=60, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """."""
    )
    consist.foamer_facts = """Metropolitan Railway electric locos"""

    return consist
