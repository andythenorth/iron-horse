"""
This file is generated from the Polar Fox project.
Don't make changes here, make them in the Polar Fox project and redistribute.
Any changes made here are liable to be over-written.
"""

from PIL import Image, ImageDraw
from copy import deepcopy
import os.path
currentdir = os.curdir


class Spritesheet:
    """
    Class holding the sprite sheet.

    @ivar sprites: The sprite sheet.
    @type sprites: L{Image}
    """
    def __init__(self, width, height, palette):
        """
        Construct an empty sprite sheet.

        @param width: Width of the sprite sheet.
        @type  width: C{int}

        @param height: Height of the sprite sheet.
        @type  height: C{int}

        @param palette: Palette of the sprite sheet.
        @type  palette: C{list} of (256*3) C{int}
        """
        self.sprites = Image.new('P', (width, height), 255)
        self.sprites.putpalette(palette)

    def save(self, output_path):
        self.sprites.save(output_path, optimize=True)


def make_cheatsheet(image, output_path, origin = None):
    block_size = 30
    palette = deepcopy(image.palette)
    rawpx = image.load()
    result = Image.new('P', (image.size[0] * block_size, image.size[1] * block_size))
    result.putpalette(palette)
    draw = ImageDraw.Draw(result)

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pen_x = x * block_size
            pen_y = y * block_size
            colour = rawpx[x, y]
            draw.rectangle([(pen_x, pen_y), (pen_x + block_size, pen_y + block_size)], fill = colour)
            if origin is not None and (x, y) == origin:
                # indicate origin; hacky, can't be bothered to learn to draw lines, so just draw more rects :P
                draw.rectangle([(pen_x, pen_y), (pen_x+block_size, pen_y+block_size)], fill = 224)
                draw.rectangle([(pen_x + 3, pen_y + 3), (pen_x + block_size - 4, pen_y + block_size - 4)], fill = colour)
            bg_size = draw.textsize(str(colour))
            text_pos_x = pen_x + 0.75 * block_size - bg_size[0]
            text_pos_y = pen_y+ block_size // 3
            draw.rectangle([(text_pos_x - 1, text_pos_y + 1), (text_pos_x + bg_size[0], text_pos_y + bg_size[1] - 2)], fill = 255)
            draw.text((text_pos_x, text_pos_y), str(colour), fill = 1)

    result.save(output_path, optimize = True)


def pixascan(image):
    """
    Optimisation method: scans an image from top left, rows first, and caches
    significant pixels from it into a list for reuse in multiple render passes.

    @param image: Source image.
    @type  image: L{PIL.Image}

    @return: Significant pixels in the image (top-left to bottom-right, rows first).
    @rtype:  A C{list} of C{tuple} (x, y, colour)
    """
    significant_pixels = []
    imagepx = image.load()
    for x in range(image.size[0]):
      for y in range(image.size[1]):
        colour = imagepx[x, y]
        if colour not in (0, 255): # don't store white, blue; assumes DOS palette
          significant_pixels.append((x, y, colour))
    return significant_pixels
