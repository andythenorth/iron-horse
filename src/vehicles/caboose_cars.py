from train import CabooseCarConsist, CabooseCar


def main():
    """
    # caboose families (family names and caboose names are arbitrary strings)
    # caboose names map to labelled spriterows, as defined in the vehicle files
    caboose_families={
        "RAIL": {
            "caboose_car": {
                "pony_caboose_car_default_1": ["caboose_1"],
                "pony_caboose_car_default_2": ["caboose_2"],
                "pony_caboose_car_default_3": ["caboose_3"],
                "pony_caboose_car_default_4": ["caboose_4"],
                "pony_caboose_car_default_5": ["caboose_5"],
                "pony_caboose_car_default_6": ["caboose_6"],
                "pony_gwr_1": ["caboose_1"],
                # "pony_gwr_1": ["caboose_1", "gwr_1"],
                "pony_railfreight_1": ["railfreight_1", "brown_1"],
                "pony_railfreight_2": ["caboose_6"],
                # "pony_railfreight_2": ["railfreight_2"],
            },
            # "goods_caboose_car": {
            # "pony_goods_caboose_car_default_1": ["caboose_1"],
            # "pony_goods_caboose_car_default_2": ["caboose_2"],
            # "pony_goods_caboose_car_default_3": ["caboose_3"],
            # "pony_goods_caboose_car_default_4": ["caboose_4"],
            # "pony_goods_caboose_car_default_5": ["caboose_5"],
            # "pony_goods_caboose_car_default_6": ["caboose_6"],
            # "pony_railfreight_1": ["railfreight_1", "brown_1"],
            # },
        },
        "NG": {
            "caboose_car": {
                "pony_ng_caboose_car_1": ["ng_caboose_1"],
                "pony_ng_caboose_car_2": ["ng_caboose_2"],
                "pony_ng_caboose_car_3": ["ng_caboose_3"],
            },
        },
    },
    # lists of one default family name per generation, ascending
    caboose_default_family_by_generation={
        "RAIL": [
            {
                "caboose_car": "pony_caboose_car_default_1",
                # "goods_caboose_car": "pony_goods_caboose_car_default_1",
            },
            {
                "caboose_car": "pony_caboose_car_default_2",
            },
            {
                "caboose_car": "pony_caboose_car_default_3",
            },
            {
                "caboose_car": "pony_caboose_car_default_4",
            },
            {
                "caboose_car": "pony_caboose_car_default_5",
            },
            {
                "caboose_car": "pony_caboose_car_default_6",
            },
        ],
        "NG": [
            # ng caboose don't have much variation
            {"caboose_car": "pony_ng_caboose_car_1"},
            {"caboose_car": "pony_ng_caboose_car_1"},
            {"caboose_car": "pony_ng_caboose_car_2"},
            {"caboose_car": "pony_ng_caboose_car_3"},
        ],
    },
    """
    # --------------- pony NG ----------------------------------------------------------------------
    # note that spriterow mapping will get redefined for different rosters and base track types
    spriterow_labels = ["ng_caboose_1", "ng_caboose_2", "ng_caboose_3"]
    caboose_families = {}

    consist = CabooseCarConsist(
        roster_id="pony",
        base_numeric_id=13140,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        spriterow_labels=spriterow_labels,
        caboose_families=caboose_families,
        sprites_complete=False,
    )

    consist.add_unit(type=CabooseCar, chassis="2_axle_ng_8px")

    consist = CabooseCarConsist(
        roster_id="pony",
        base_numeric_id=10330,
        gen=1,
        subtype="B",
        base_track_type_name="NG",
        spriterow_labels=spriterow_labels,
        caboose_families=caboose_families,
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
        "gwr_1",
        "brown_1",
        "railfreight_1",
        # "railfreight_2",
    ]
    caboose_families = {}

    consist = CabooseCarConsist(
        roster_id="pony",
        base_numeric_id=10320,
        gen=1,
        subtype="A",
        spriterow_labels=spriterow_labels,
        caboose_families=caboose_families,
        docs_image_spriterow=0,  # !! support for forcing docs image, may not be needed with randomised buy menu sprite ??
        sprites_complete=False,
    )

    consist.add_unit(type=CabooseCar, chassis="2_axle_caboose_16px")

    consist = CabooseCarConsist(
        roster_id="pony",
        base_numeric_id=11250,
        gen=1,
        subtype="B",
        spriterow_labels=spriterow_labels,
        caboose_families=caboose_families,
        docs_image_spriterow=0,  # !! support for forcing docs image, may not be needed with randomised buy menu sprite ??
        sprites_complete=False,
    )

    consist.add_unit(type=CabooseCar, chassis="4_axle_caboose_24px")
