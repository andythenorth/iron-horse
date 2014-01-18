#!/usr/bin/env python

from time import time
start = time()

print "[BUILD] build_iron_horse.py"

import iron_horse
import utils

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import codecs # used for writing files - more unicode friendly than standard open() module

# render the nml file
import render_nml
render_nml.main()

# render the graphics
import render_graphics
render_graphics.main()

# render the lang files
import render_lang
render_lang.main()

# render the docs
import render_docs

print (time() - start)
