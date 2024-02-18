from train import EngineConsist, SteamEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="keen",
        base_numeric_id=470,
        name="0-6-0+0-6-0 Keen",
        role="heavy_freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 1800,
        },
        random_reverse=True,
        gen=3,
        intro_year_offset=-13,  # introduce much earlier than gen epoch by design
        fixed_run_cost_points=240,  # adjust to match similar engines of same gen
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=SteamEngineUnit,
        weight=58,
        vehicle_length=5,
        spriterow_num=0,
        repeat=2,
    )

    consist.description = """Gallop apace, you fiery-footed steeds."""
    consist.foamer_facts = """18in Hunslet tanks, Austerity tanks, LNER J94 Class"""

    return consist
