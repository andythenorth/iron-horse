from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="keen",
        base_numeric_id=470,
        name="0-6-0+0-6-0 Keen",
        role="heavy_freight",
        role_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1800,
        },
        random_reverse=True,
        gen=3,
        intro_year_offset=-13,  # introduce much earlier than gen epoch by design
        fixed_run_cost_points=140,  # minor run cost bonus as default algorithm makes run cost too high
        additional_liveries=[],
        sprites_complete=False,
        sprites_additional_liveries_needed=True, # nightshade / nighthawk?
    )

    consist.add_unit(
        type=SteamEngineUnit,
        weight=55,
        vehicle_length=5,
        spriterow_num=0,
        repeat=2,
    )

    # !! what are these supposed to be?
    # some 0-6-0t thing?  Classic jinty? Pannier?
    # maybe Austerity J94 is simplest?
    # 1937 18in Hunslet https://www.irsociety.co.uk/Archives/23/18in_Hunslets.htm
    # https://preservedbritishsteamlocomotives.com/hunslet-works-no-1440-airdale-no-3-0-6-0st/
    # or the chunky bagnalls? https://www.flickr.com/photos/60956647@N02/15691831650
    consist.description = """Gallop apace, you fiery-footed steeds."""
    consist.foamer_facts = """"""

    return consist
