from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="doister",
        base_numeric_id=280,
        name="2-6-0 Doister",
        role="heavy_freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 1500,  # slightly less than the Swift (and lighter engine)
        },
        tractive_effort_coefficient=0.2,
        fixed_run_cost_points=140,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=2,
        intro_year_offset=10,  # introduce later than gen epoch by design
        caboose_family="gwr_1",
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=82, vehicle_length=6, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=30, vehicle_length=4, spriterow_num=1
    )

    consist.description = """If we do each thing calmly and carefully we will get it done quicker and with much less fuss."""
    # seems to be it was intended to be a GCR-ish big 2-6-0 https://www.steamindex.com/media/arle2.jpg
    # or the baldwin imports? https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.gettyimages.com%2Fid%2F90748460%2Fphoto%2Fmidland-railway-2-6-0-steam-locomotive-no-2.jpg%3Fs%3D1024x1024%26w%3Dgi%26k%3D20%26c%3DB24UM2P0PvqtHOeSH8ZiMwO1bvidKL14HeIQZR0vF9U%3D&imgrefurl=https%3A%2F%2Fwww.gettyimages.ca%2Fdetail%2Fnews-photo%2Fmidland-railway-2-6-0-steam-locomotive-no-2510-c-1900-this-news-photo%2F90748460&tbnid=NMcvMgOoPncnKM&vet=12ahUKEwin4ObrndL9AhUenCcCHcXkAwYQMygCegUIARDDAQ..i&docid=CWUDrSzVUrJ1rM&w=1024&h=804&q=gcr%20baldwin%202-6-0&ved=2ahUKEwin4ObrndL9AhUenCcCHcXkAwYQMygCegUIARDDAQ
    # https://www.lner.info/locos/K/k1k2.php
    #
    # would a 2-6-2 be better?
    consist.foamer_facts = """"""

    return consist
