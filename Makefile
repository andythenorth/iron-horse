# Various needed programs
GIT = git
PYTHON3 = python3
SED = sed
ZIP = zip

NMLC = nmlc
GRFCODEC = grfcodec
GRFID = grfid

GIT_INFO = $(PYTHON3) src/polar_fox/git_info.py
FILL_TEMPLATE = bin/fill-template
FIND_FILES = bin/find-files
MK_ARCHIVE = bin/mk-archive


# Project details
PROJECT_NAME = iron-horse

GRAPHICS_TARGET = generated/graphics/make_target
LANG_DIR = generated/lang
LANG_TARGET = $(LANG_DIR)/english.lng
NML_FILE = generated/iron-horse.nml
NML_FLAGS = -l $(LANG_DIR) --verbosity=4

-include Makefile.local

EXPORTED = no
ifeq ($(strip $(EXPORTED)),no)
  # Not exported source, therefore regular checkout
  REPO_INFO = $(shell $(GIT_INFO))
  REPO_REVISION = $(word 1,$(REPO_INFO))
  REPO_VERSION = $(word 2,$(REPO_INFO))
else
  # Exported version, lines below should get modified in 'bundle_src' target
  REPO_REVISION = ${exported_revision}
  REPO_VERSION = ${exported_version}
endif

REPO_TITLE = "$(PROJECT_NAME) $(REPO_VERSION)"
PROJECT_VERSIONED_NAME = $(PROJECT_NAME)-$(REPO_VERSION)
# Args for faster compiles: PW=n (num pool workers) SC=bool (suppress cargo sprites) SD=bool (suppress docs)
ARGS = '$(PW)' '$(ROSTER)' '$(SC)' '$(SD)'

NFO_FILE = generated/$(PROJECT_NAME).nfo
GRF_FILE = generated/$(PROJECT_NAME).grf
TAR_FILE = $(PROJECT_VERSIONED_NAME).tar
ZIP_FILE = $(PROJECT_VERSIONED_NAME).zip
MD5_FILE = $(PROJECT_NAME).check.md5

HTML_DOCS = docs

SOURCE_NAME = $(PROJECT_VERSIONED_NAME)-source
BUNDLE_DIR = bundle_dir

# Build rules
.PHONY: default graphics lang nml grf tar bundle_tar bundle_zip bundle_src clean
default: html_docs grf
# bundle needs to clean first to ensure we don't use outdated/cached version info
bundle_tar: clean tar
bundle_zip: $(ZIP_FILE)
release: bundle_tar copy_docs_to_grf_farm
graphics: $(GRAPHICS_TARGET)
lang: $(LANG_TARGET)
nml: $(NML_FILE)
nfo: $(NFO_FILE)
grf: $(GRF_FILE)
tar: $(TAR_FILE)
html_docs: $(HTML_DOCS)

# default num. pool workers for python compile,
# default is 0 to disable multiprocessing (also avoids multiprocessing pickle failures masking genuine python errors)
PW = 0
# option to suppress cargo sprites, makes minor difference to compile time
SC = 'False'
ROSTER = ALL
# remove the @ for more verbose output (@ suppresses command output)
_V ?= @

$(GRAPHICS_TARGET): $(shell $(FIND_FILES) --ext=.py --ext=.png src)
	$(_V) $(PYTHON3) src/render_graphics.py $(ARGS)
	$(_V) touch $(GRAPHICS_TARGET)

$(LANG_TARGET): $(shell $(FIND_FILES) --ext=.py --ext=.pynml --ext=.lng src)
	$(_V) $(PYTHON3) src/render_lang.py $(ARGS)

$(HTML_DOCS): $(GRAPHICS_TARGET) $(LANG_TARGET) $(shell $(FIND_FILES) --ext=.py --ext=.pynml --ext=.pt --ext=.lng --ext=.png src)
	$(_V) $(PYTHON3) src/render_docs.py $(ARGS)

$(NML_FILE): $(shell $(FIND_FILES) --ext=.py --ext=.pynml src)
	$(_V) $(PYTHON3) src/render_nml.py $(ARGS)

# nmlc is used to compile a nfo file only, which is then used by grfcodec
# this means that the (relatively slow) nmlc stage can be skipped if the nml file is unchanged (only graphics changed)
$(NFO_FILE): $(LANG_TARGET) $(NML_FILE) | $(GRAPHICS_TARGET)
	$(NMLC) $(NML_FLAGS) --nfo=$(NFO_FILE) $(NML_FILE) --no-optimisation-warning

# N.B grf codec can't compile into a specific target dir, so after compiling, move the compiled grf to appropriate dir
# grfcodec -n was tried, but was slower and produced a large grf file
$(GRF_FILE): $(GRAPHICS_TARGET) $(NFO_FILE)
	$(GRFCODEC) -s -e -c -g 2 $(PROJECT_NAME).grf generated
	mv $(PROJECT_NAME).grf $(GRF_FILE)

$(TAR_FILE): $(GRF_FILE) $(HTML_DOCS)
# the goal here is a sparse tar for distribution
	# create an intermediate dir, and copy in what we need
	mkdir $(PROJECT_VERSIONED_NAME)
	cp docs/readme.txt $(PROJECT_VERSIONED_NAME)
	cp docs/changelog.txt $(PROJECT_VERSIONED_NAME)
	cp docs/license.txt $(PROJECT_VERSIONED_NAME)
	cp $(GRF_FILE) $(PROJECT_VERSIONED_NAME)
	$(MK_ARCHIVE) --tar --output=$(TAR_FILE) $(PROJECT_VERSIONED_NAME)
	# delete the intermediate dir
	rm -r $(PROJECT_VERSIONED_NAME)

$(ZIP_FILE): $(TAR_FILE)
	$(ZIP) -9rq $(ZIP_FILE) $(TAR_FILE) >/dev/null

$(MD5_FILE): $(GRF_FILE)
	$(GRFID) -m $(GRF_FILE) > $(MD5_FILE)

bundle_src: $(MD5_FILE)
	if test -d $(BUNDLE_DIR); then rm -r $(BUNDLE_DIR); fi
	mkdir $(BUNDLE_DIR)
	$(GIT) archive -t files $(BUNDLE_DIR)/src
	$(FILL_TEMPLATE) --template=Makefile \
		--output=$(BUNDLE_DIR)/src/Makefile \
		"exported_revision=$(REPO_REVISION)" \
		"exported_version=$(REPO_VERSION)"
	$(SED) -i -e 's/^EXPORTED = no/EXPORTED = yes/' $(BUNDLE_DIR)/src/Makefile
	$(MK_ARCHIVE) --tar --output=$(SOURCE_NAME).tar --base=$(SOURCE_NAME) \
		`$(FIND_FILES) $(BUNDLE_DIR)/src` $(MD5_FILE)

# this expects to find a '../../grf.farm' path relative to the project, and will fail otherwise
copy_docs_to_grf_farm:
	$(_V) $(PYTHON3) src/polar_fox/grf_farm.py $(PROJECT_NAME)

# this is a macOS-specifc install location; the pre-2017 Makefile handled multiple platforms, that could be restored if needed
# remove first, OpenTTD does not like having the _contents_ of the current file change under it, but will handle a removed-and-replaced file correctly
install: default
	rm ~/Documents/OpenTTD/newgrf/$(PROJECT_NAME).grf
	cp $(GRF_FILE) ~/Documents/OpenTTD/newgrf/

clean:
	$(_V) echo "[CLEANING]"
	$(_V) for f in .chameleon_cache .nmlcache src/__pycache__ src/*/__pycache__ docs generated \
	$(GRF_FILE) $(TAR_FILE) $(ZIP_FILE) $(MD5_FILE) $(BUNDLE_DIR) $(SOURCE_NAME).tar;\
	do if test -e $$f;\
	   then rm -r $$f;\
	   fi;\
	done
	$(_V) echo "[DONE]"
