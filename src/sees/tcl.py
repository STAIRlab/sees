import sys
import json
from functools import partial
from sees import config, render
from sees.parser import parse_args
from sees.errors import RenderError

def _render(*args, rt=None):
    try:
        config = parse_args(["render", *args])
#       print(config)
        if config is None:
            return ""
        if "verbose" in config and config["verbose"]:
            print(config)

        config["sam_file"] = rt.to_dict()
        render(**config)

    except RenderError:
        print(e, file=sys.stderr)

    return ""

def add_commands(rt):
    try:
        rt._tcl.createcommand("sees::render", partial(_render, rt=rt))
    except:
        pass


