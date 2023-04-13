"""
This file is generated from the Polar Fox project.
Don't make changes here, make them in the Polar Fox project and redistribute.
Any changes made here are liable to be over-written.
"""

#!/usr/bin/env python3

import subprocess


def exe_cmd(cmd):
    try:
        output = subprocess.run(
            cmd,
            env=None,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            universal_newlines=True,
        ).stdout
        lines = output.splitlines()
        return lines
    except:
        return ["undefined"]


def get_revision():
    # revision is simply the count of revs in the current branch
    # this won't be perfect in all cases, but there's no possible way to produce a perfect single rev with git
    # so this is good enough
    return exe_cmd(["git", "rev-list", "--count", "HEAD"])[0]


def get_version():
    # for the version we just use git describe, which gives us a recent tag or so
    return exe_cmd(["git", "describe"])[0]


def get_tag_exact_match():
    # are we on a specific tag? (returns tag if true, otherwise errors)
    return exe_cmd(["git", "describe", "--tags", "--exact-match"])[0]


def get_monorepo_tag_parts():
    # some projects use monorepos to release multiple artefacts
    # each released artefact has its own tag subpath, e.g.
    # horse/1.2.3
    # ibex/3.4.5
    # git will create these tags as actual filesystem subpaths in .git/refs/tags/
    tag = get_tag_exact_match()
    if tag != "undefined":
        # consumers probably assume we only have one level of nesting here, but don't worry about it...
        # ...if the split produces too many parts consumer release scripts will probably fail, but deal with that later if it happens
        parts = tag.split("/")
        return parts
    else:
        # very clunky return to ensure we get the expected number of printed results
        return ["undefined", "undefined"]

def run():
    # for the default case we just print the results, this is used by e.g. Makefiles
    # for python cases, use the get_foo methods directly
    # note that we print the leading and trailing parts of the tag in the monorepo case (baked-in assumption that only 2 parts exist)
    print(get_revision(), get_version(), get_tag_exact_match(), ' '.join(get_monorepo_tag_parts()))


if __name__ == "__main__":
    run()
