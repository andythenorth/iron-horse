#!/usr/bin/env python

from time import time

print "[BUILD] build_iron_horse.py"

import iron_horse
import utils

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

# render the nml file
start = time()
import render_nml
render_nml.main()
print format((time() - start), '.2f')+'s'

# render the graphics
start = time()
import render_graphics
render_graphics.main()
print format((time() - start), '.2f')+'s'

# render the lang files
start = time()
import render_lang
render_lang.main()
print format((time() - start), '.2f')+'s'

# render the docs
start = time()
import render_docs
render_docs.main()
print format((time() - start), '.2f')+'s'
