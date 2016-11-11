from graphics_processor import graphics_constants

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
