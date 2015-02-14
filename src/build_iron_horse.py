#!/usr/bin/env python

from time import time

print "[BUILD] build_iron_horse.py"

import utils

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

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

# render the nml file
start = time()
import render_nml_nfo
render_nml_nfo.main()
elapsed_time = (time() - start)
print format(elapsed_time, '.2f')+'s'
if elapsed_time > 2 and render_nml_nfo.everything_dirty == False:
    utils.echo_message("Slow nml rendering?  Try the COMPILE_FASTER=True make flag if you're only changing vehicle properties")

# render the docs
start = time()
import render_docs
render_docs.main()
print format((time() - start), '.2f')+'s'
