import graphics_constants

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
    AORE = {170: 42, 171: 123, 172: 74, 173: 125, 174: 162, 175: 126, 176: 78}
    IORE = {170: 75, 171: 76, 172: 123, 173: 122, 174: 124, 175: 74, 176: 104}
    CORE = {170: 1, 171: 32, 172: 25, 173: 27, 174: 34, 175: 56, 176: 59}
    GRVL = {170: 6, 171: 4, 172: 7, 173: 8, 174: 21, 175: 11, 176: 12}
    SAND = {170: 108, 171: 64, 172: 65, 173: 197, 174: 36, 175: 196, 176: 197}
    COAL = {170: 1, 171: 2, 172: 3, 173: 4, 174: 5, 175: 5, 176: 6}

    # we just return a fixed-order tuple here, don't worry about the labels...
    # ...we have to manually specify the spriterow<->cargo label mapping in the wagon definition anyway
    return (AORE, IORE, CORE, GRVL, SAND, COAL)
