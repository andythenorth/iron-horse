from train import EngineConsist, DieselEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="f40ph",
        base_numeric_id=22010,
        name="F40PH",
        role="branch_express",
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 1800,
        },
        random_reverse=True,
        fixed_run_cost_points=140,  # substantial cost bonus as a mixed traffic engine
        gen=4,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=110, vehicle_length=6, spriterow_num=0
    )

    consist.description = """"""
    consist.foamer_facts = """"""

    return consist
