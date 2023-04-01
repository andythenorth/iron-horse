from train import EngineConsist, ElectroDieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="constance",
        base_numeric_id=8220,
        name="Constance",
        role="heavy_express",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 3600,
            "AC": 3600, # yes it's the same on both, just the effect changes; this is a cheat to get an extra option at 3.5k for both dieeel and electric
        },
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=6,
        intro_year_offset=-2,  # introduce earlier than gen epoch by design
        additional_liveries=["SWOOSH_LESS", "SWOOSH", "FREIGHTLINER_GBRF"],
        sprites_complete=False,
        sprites_additional_liveries_needed=True, # banger blue?
    )

    consist.add_unit(
        type=ElectroDieselEngineUnit, weight=95, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """Runs like a Swiss watch."""
    )
    consist.foamer_facts = """Siemens Vectron Dual Mode"""

    return consist
