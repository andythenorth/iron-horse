from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="nemesis",
        base_numeric_id=8230,
        name="Lion",
        role="super_heavy_freight",
        role_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 2950,
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=10,  # let's be later for this one
        additional_liveries=["BANGER_BLUE", "SWOOSH"],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=60, vehicle_length=8,
    )

    consist.description = """Good horses make short miles."""
    consist.foamer_facts = """BRCW / BR D0260 Falcon prototype."""

    return consist
