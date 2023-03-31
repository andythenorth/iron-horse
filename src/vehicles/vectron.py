from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="vectron",
        base_numeric_id=8220,
        name="Vectron",
        role="heavy_express",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 3450,
        },
        random_reverse=True,
        gen=6,
        intro_year_offset=-2,  # introduce earlier than gen epoch by design
        additional_liveries=[],
        sprites_complete=False,
        sprites_additional_liveries_needed=True, # banger blue?
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=95, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """"""
    )
    consist.foamer_facts = """"""

    return consist
