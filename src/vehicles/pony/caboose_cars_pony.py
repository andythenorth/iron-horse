from train import CabooseCarConsist, CabooseCar


def main(roster_id, **kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------
    # caboose names map to labelled spriterows, as defined in the vehicle files
    # note that spriterow mapping will need redefined for each roster and base track type
    # names are arbitrary strings, except for 'default_1', 'default_2', etc which must match the number of generations for this base track type in the roster
    spriterow_labels = [
        "cc_enclosed_1",
        "cc_enclosed_2",
        "cc_enclosed_3",
        "cc_asymmetric_1",
        "cc_asymmetric_2",
        "cc_asymmetric_3",
        "brown_enclosed_1",
        "brown_enclosed_2",
        "brown_enclosed_3",
        "brown_asymmetric_1",
        "brown_asymmetric_2",
        "brown_asymmetric_3",
    ]
    # note that probability of a specific type within a family can be increased by repeating it in the list for that family
    caboose_families = {
        "default_1": [
            "cc_enclosed_1",
            "brown_enclosed_1",
            "cc_asymmetric_1",
            "brown_asymmetric_1",
        ],
        "default_2": [
            "cc_enclosed_2",
            "brown_enclosed_2",
            "cc_asymmetric_2",
            "brown_asymmetric_2",
        ],
        "default_3": [
            "cc_enclosed_3",
            "brown_enclosed_3",
            "cc_asymmetric_3",
            "brown_asymmetric_3",
        ],
        "default_4": [
            "cc_enclosed_3",
            "brown_enclosed_3",
            "cc_asymmetric_3",
            "brown_asymmetric_3",
        ],
    }
    # these should match the number of default families, in order
    buy_menu_sprite_pairs = [
        ("cc_enclosed_1", "brown_enclosed_1"),
        ("cc_enclosed_2", "brown_enclosed_3"),
        ("cc_enclosed_3", "brown_enclosed_3"),
        ("cc_enclosed_3", "brown_enclosed_3"),
    ]

    consist_factory = CabooseCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23690,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        spriterow_labels=spriterow_labels,
        caboose_families=caboose_families,
        buy_menu_sprite_pairs=buy_menu_sprite_pairs,
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="CabooseCar", chassis="2_axle_ng_8px")

    result.append(consist_factory)

    consist_factory = CabooseCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=26270,
        gen=1,
        subtype="B",
        base_track_type_name="NG",
        spriterow_labels=spriterow_labels,
        caboose_families=caboose_families,
        buy_menu_sprite_pairs=buy_menu_sprite_pairs,
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="CabooseCar", chassis="4_axle_ng_16px")

    # --------------- standard gauge ---------------------------------------------------------------    # caboose names map to labelled spriterows, as defined in the vehicle files
    # note that spriterow mapping will need redefined for each roster and base track type
    # names are arbitrary strings, except for 'default_1', 'default_2', etc which must match the number of generations for this base track type in the roster
    spriterow_labels = [
        "cc_enclosed_1",
        "cc_enclosed_2_3",
        "cc_enclosed_4",
        "cc_enclosed_5",
        "cc_enclosed_6",
        "cc_open_1",
        "cc_open_2",
        "cc_open_3",
        "cc_gwr_1",
        "brown_enclosed_1",
        "brown_enclosed_2_3",
        "brown_enclosed_4",
        "brown_open_1",
        "brown_gwr_1",
        "grey_enclosed_1",
        "grey_enclosed_2_3",
        "grey_open_1",
        "grey_gwr_1",
        "railfreight_enclosed_1",
        "railfreight_open_1",
        "railfreight_enclosed_2",
        "railfreight_open_2",
    ]
    # note that probability of a specific type within a family can be increased by repeating it in the list for that family
    caboose_families = {
        "default_1": [
            "cc_enclosed_1",
            "brown_enclosed_1",
            "grey_enclosed_1",
            "grey_enclosed_1",
            "cc_open_1",
            "brown_open_1",
            "grey_open_1",
        ],
        "default_2": [
            "cc_enclosed_2_3",
            "brown_enclosed_2_3",
            "grey_enclosed_2_3",
            "cc_open_1",
            "brown_open_1",
            "grey_open_1",
        ],
        "default_3": [
            "cc_enclosed_2_3",
            "brown_enclosed_2_3",
            "grey_enclosed_2_3",
            "cc_open_1",
            "cc_open_1",
            "brown_open_1",
            "grey_open_1",
        ],
        "default_4": [
            "cc_enclosed_4",
            "brown_enclosed_4",
            "brown_enclosed_4",
            "brown_open_1",
            "brown_open_1",
            "cc_open_1",
            "cc_open_2",
        ],
        "default_5": [
            "cc_enclosed_5",
            "brown_open_1",
            "cc_open_1",
            "cc_open_2",
            "cc_open_2",
            "cc_open_3",
        ],
        "default_6": [
            "cc_enclosed_6",
            "cc_enclosed_5",
            "cc_open_2",
            "cc_open_3",
            "cc_open_3",
        ],
        "gwr_1": [
            "cc_gwr_1",
            "cc_gwr_1",
            "brown_gwr_1",
            "grey_gwr_1",
            "grey_enclosed_2_3",
        ],
        "railfreight_1": [
            "railfreight_enclosed_1",
            "railfreight_open_1",
            "railfreight_open_1",
            "brown_enclosed_4",
            "brown_open_1",
            "brown_open_1",
        ],
        "railfreight_2": [
            "railfreight_enclosed_2",
            "railfreight_open_2",
            "cc_enclosed_6",
            "cc_open_1",
            "brown_open_1",
        ],
    }
    # these should match the number of default families, in order
    buy_menu_sprite_pairs = [
        ("cc_enclosed_1", "brown_open_1"),
        ("cc_enclosed_2_3", "brown_enclosed_2_3"),
        ("cc_enclosed_2_3", "brown_open_1"),
        ("cc_enclosed_4", "cc_open_1"),
        ("cc_enclosed_5", "cc_open_1"),
        ("cc_enclosed_6", "cc_open_1"),
    ]

    consist_factory = CabooseCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23270,
        gen=1,
        subtype="A",
        spriterow_labels=spriterow_labels,
        caboose_families=caboose_families,
        buy_menu_sprite_pairs=buy_menu_sprite_pairs,
        docs_image_spriterow=3,
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="CabooseCar", chassis="2_axle_caboose_16px")

    result.append(consist_factory)

    consist_factory = CabooseCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23280,
        gen=1,
        subtype="B",
        spriterow_labels=spriterow_labels,
        caboose_families=caboose_families,
        buy_menu_sprite_pairs=buy_menu_sprite_pairs,
        docs_image_spriterow=3,
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="CabooseCar", chassis="4_axle_caboose_24px")

    result.append(consist_factory)

    return result
