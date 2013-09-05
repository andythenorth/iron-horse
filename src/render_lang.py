print "[RENDER LANG] render_lang.py"

import fish
import utils

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import codecs # used for writing files - more unicode friendly than standard open() module

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
lang_templates = PageTemplateLoader(os.path.join(currentdir, 'lang_src'))

ships = fish.get_ships_in_buy_menu_order()
# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)

# this is a brutally simple way of specifying which languages are available
# could also read the lang dir and work it out from .pylng extensions, but meh, tmwftlb
translated_languages = ('english',)
for i in translated_languages:
    #compile strings to single lang file - english
    lang_template = lang_templates[i + '.pylng']

    lang = codecs.open(os.path.join('lang', i + '.lng'), 'w','utf8')
    lang.write(lang_template(ships=ships, repo_vars=repo_vars))
    lang.close()
