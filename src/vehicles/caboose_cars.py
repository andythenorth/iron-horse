from train import CabooseCarConsist, CabooseCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------
    # note that spriterow mapping will get redefined for different rosters and base track types
    spriterow_labels = ["ng_caboose_1", "ng_caboose_2", "ng_caboose_3"]

    consist = CabooseCarConsist(
        roster_id="pony",
        base_numeric_id=4100,
        gen=1,
        subtype="A",
        base_track_type="NG",
        spriterow_labels=spriterow_labels,
        sprites_complete=False,
    )

    consist.add_unit(type=CabooseCar, chassis="2_axle_ng_8px")

    consist = CabooseCarConsist(
        roster_id="pony",
        base_numeric_id=1290,
        gen=1,
        subtype="B",
        base_track_type="NG",
        spriterow_labels=spriterow_labels,
        sprites_complete=False,
    )

    consist.add_unit(type=CabooseCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------
    # note that spriterow mapping will get redefined for different rosters and base track types
    spriterow_labels = [
        "caboose_1",
        "caboose_2",
        "caboose_3",
        "caboose_4",
        "caboose_5",
        "caboose_6",
        #"gwr_1",
        #"brown_1",
        #"railfreight_1",
        #"railfreight_2",
    ]

    consist = CabooseCarConsist(
        roster_id="pony",
        base_numeric_id=1280,
        gen=1,
        subtype="A",
        spriterow_labels=spriterow_labels,
        docs_image_spriterow=6,
        sprites_complete=False,
    )

    consist.add_unit(type=CabooseCar, chassis="2_axle_caboose_16px")

    consist = CabooseCarConsist(
        roster_id="pony",
        base_numeric_id=2210,
        gen=1,
        subtype="B",
        spriterow_labels=spriterow_labels,
        docs_image_spriterow=6,
        sprites_complete=False,
    )

    consist.add_unit(type=CabooseCar, chassis="4_axle_caboose_24px")
