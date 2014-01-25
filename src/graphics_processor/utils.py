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
