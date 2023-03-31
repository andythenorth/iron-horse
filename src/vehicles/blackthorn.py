from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="blackthorn",
        base_numeric_id=12510,
        name="Blackthorn",
        role="heavy_freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 3450,
        },
        random_reverse=True,
        gen=6,
        default_livery_extra_docs_examples=[("COLOUR_MAUVE", "COLOUR_CREAM")],
        additional_liveries=[],
        sprites_complete=True,
        sprites_additional_liveries_needed=True, # ??
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=124, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """I've refitted the Grid for a longer life.  Still not bad at all."""
    )
    consist.foamer_facts = """GBRF Class 69 (re-engineered BR Class 56)"""

    return consist
