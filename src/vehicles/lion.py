from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="lion",
        base_numeric_id=8230,
        name="Lion",
        role="super_heavy_freight",
        role_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 3300, # first high HP diesel in this roster??
        },
        speed=87,  # for lolz
        random_reverse=True,
        gen=4,
        intro_year_offset=12,  # let's be later for this one, it's long-lived also
        additional_liveries=["BANGER_BLUE", "SWOOSH"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=132,
        vehicle_length=8,
        effect_offsets=[(0, 1), (0, -1)],  # double the smoke eh?
    )

    consist.description = """Good horses make short miles."""
    consist.foamer_facts = """BRCW / BR D0260 Lion prototype, Brush HS4000 Kestrel prototype"""

    return consist
