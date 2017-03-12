# Various needed programs
PYTHON3 = python3
NMLC = nmlc

HG_INFO = bin/hg-info
FIND_FILES = bin/find-files
MK_ARCHIVE = bin/mk-archive


# Project details
PROJECT_NAME = iron-horse
SOURCES=$(shell $(FIND_FILES) --ext=.py src)

NML_FILE = generated/iron-horse.nml
NML_FLAGS =-c -l generated/lang

GRF_FILE = $(PROJECT_NAME).grf
TAR_FILE = $(PROJECT_NAME).tar

DOC_FILES = docs/license.txt docs/changelog.txt

REPO_INFO = $(shell $(HG_INFO) --num-id --version)
REPO_REVISION = $(word 1,$(REPO_INFO))
REPO_VERSION = $(word 2,$(REPO_INFO))
REPO_TITLE = "$(PROJECT_NAME) $(REPO_VERSION)"
PROJECT_VERSIONED_NAME = "$(PROJECT_NAME)-$(REPO_VERSION)"


default: $(GRF_FILE)
tar: $(TAR_FILE)

 # default num. pool workers for python compile,
 # default is 0 to disable multiprocessing (also avoids multiprocessing pickle failures masking genuine python errors)
PW = 0
ROSTER = *

$(NML_FILE): $(SOURCES)
	$(PYTHON3) src/build_iron_horse.py '$(REPO_TITLE)' '$(REPO_REVISION)' '$(PW)' '$(ROSTER)'

$(GRF_FILE): $(NML_FILE)
	$(NMLC) $(NML_FLAGS) --grf=$(GRF_FILE) $(NML_FILE)

$(TAR_FILE): $(GRF_FILE)
	$(MK_ARCHIVE) --tar --output=$(TAR_FILE) --flatten --base=$(PROJECT_VERSIONED_NAME) $(DOC_FILES) $(GRF_FILE)

