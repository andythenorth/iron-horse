def make_colour_map(input, output, map_size):
    result = {}
    for i in range(map_size):
        result[input + i] = output + i
    return result
