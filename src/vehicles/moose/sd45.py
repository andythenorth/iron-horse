from train import EngineConsist


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="sd45",
        base_numeric_id=22020,
        name="SD45",
        subrole="super_heavy_freight",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 3600,  # first high HP diesel in this roster??
        },
        random_reverse=True,
        gen=4,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        class_name="DieselEngineUnit",
        weight=160,
        vehicle_length=8,
    )

    consist.description = """"""
    consist.foamer_facts = (
        """"""
    )

    return consist
