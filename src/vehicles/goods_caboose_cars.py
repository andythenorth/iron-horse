from train import GoodsCabooseCarConsist, CabooseCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    # note that spriterow mapping will get redefined for different rosters and base track types
    spriterow_labels = [
        "caboose_1",
        "caboose_2",
        "caboose_3",
        "caboose_4",
        "caboose_5",
        "caboose_6",
        "brown_1",
        "railfreight_1",
    ]

    consist = GoodsCabooseCarConsist(
        roster_id="pony",
        base_numeric_id=7580,
        gen=1,
        subtype="A",
        spriterow_labels=spriterow_labels,
        docs_image_spriterow=3,
        sprites_complete=False,
    )

    consist.add_unit(type=CabooseCar, chassis="2_axle_caboose_16px")

    consist = GoodsCabooseCarConsist(
        roster_id="pony",
        base_numeric_id=7590,
        gen=1,
        subtype="B",
        spriterow_labels=spriterow_labels,
        docs_image_spriterow=3,
        sprites_complete=False,
    )

    consist.add_unit(type=CabooseCar, chassis="4_axle_caboose_24px")
