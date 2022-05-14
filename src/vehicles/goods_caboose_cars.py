from train import GoodsCabooseCarConsist, CabooseCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    consist = GoodsCabooseCarConsist(
        roster_id="pony",
        base_numeric_id=7580,
        gen=1,
        subtype="A",
        docs_image_spriterow=6,
        sprites_complete=False,
    )

    consist.add_unit(type=CabooseCar, chassis="2_axle_caboose_16px")

    consist = GoodsCabooseCarConsist(
        roster_id="pony",
        base_numeric_id=7590,
        gen=1,
        subtype="B",
        docs_image_spriterow=6,
        sprites_complete=False,
    )

    consist.add_unit(type=CabooseCar, chassis="4_axle_caboose_24px")
