from graphics_processor import graphics_constants

def make_colour_map(input, output, map_size):
    result = {}
    for i in range(map_size):
        result[input + i] = output + i
    return result

def get_container_recolour_maps():
    CC1 = graphics_constants.CC1
    CC2 = graphics_constants.CC2
    map_1 = make_colour_map(170, CC1, 8)
    map_1.update(make_colour_map(42, CC1, 8))

    map_2 = make_colour_map(170, CC2, 8)
    map_2.update(make_colour_map(42, CC2, 8))

    map_3 = make_colour_map(170, 8, 8)
    map_3.update(make_colour_map(42, 8, 8))

    return (map_1, map_2, map_3)


def get_bulk_cargo_recolour_maps():
    # this is interim glue to the old methods whilst porting the Road Hog graphics processor to Iron Horse
    # ...we have to manually specify the spriterow<->cargo label mapping in the wagon definition anyway
    # GRVl is also reused for generic unknown cargos, and is in position 0 for this reason
    # (there is no mapping for unknown cargos, just uses first spriteset)
    # ^^ all of that will be unnecessary when Road Hog processor is ported; this can then be deleted
    result = []
    for label in ['GRVL', 'IORE', 'CORE', 'AORE', 'SAND', 'COAL', 'CLAY', 'SCMT', 'PHOS', 'CASS', 'LIME', 'MNO2', 'NITR', 'PORE', 'POTA', 'SGBT']:
        for map in graphics_constants.bulk_cargo_recolour_maps:
            if map[0] == label:
                result.append(map[1])
    return result
