from pathlib import Path
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory

from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles.pygments import style_from_pygments_cls
from pygments.lexers.tcl import TclLexer
import pygments.styles
from pygments.styles import get_style_by_name

from .unix import file_util_commands

# style = style_from_pygments_cls(get_style_by_name('pastie'))
style = style_from_pygments_cls(get_style_by_name('nord'))


completions = {
        'model': {
            'basic': {
                '1': {1},
                '2': {2, 3},
                '3': {3, 6},
            },
        },
        'node': None,
        'element': {
            "ForceBeamColumn"
        },
        'exit': None,
}

intro = """
    OpenSees -- Open System For Earthquake Engineering Simulation
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            Pacific Earthquake Engineering Research Center
"""

intro2= """
                   ╔═╗╔═╗╔═╗╔═╗  ╔══╔═╗╔═╗ ╔══
                   ╚═╝╠═╝╚══╝ ║ ═╝  ╚══╚═══╝
   ═══════════════════╝Berkeley, California ══════════════════════
"""

intro = """
                   ┌─┐┌─┐┌─┐┌─┐  ┌──┌─┐┌─┐ ┌──
                   └─┘├─┘└──┘ │ ─┘  └──└───┘
   ───────────────────┘Berkeley, California ──────────────────────
                           © UC Regents
"""

PROMPT = "opensees \N{WHITE PARALLELOGRAM} "

def nested_prompt(session=None, _prompt=None, inputs="", depth=1, ret=True, **kwds):
    if _prompt is None: _prompt = "  "*depth

    if session is None:
        inputs = "\n".join((inputs, prompt(_prompt, **kwds)))
    else:
        inputs = "\n".join((inputs, session.prompt(_prompt, **kwds)))

    if inputs[-1] == "{":
        while True:
            inputs = nested_prompt(session=None, inputs=inputs, depth=depth+1, ret=False, **kwds)
            if inputs[-2:] == "\n}":
                inputs = inputs + "\n"
                break

    return inputs

if __name__ == "__main__":
    import opensees
    #files, opts, argi = parse_args(sys.argv)
    import time, sys
    use_vi = True
    tcl = opensees.tcl.TclRuntime(verbose=False) #opts["verbose"])
    tcl.eval(file_util_commands)
    completions.update({k: None for k in tcl.eval("info commands").split()})
    # tcl.eval(f"set argc {len(sys.argv) - 2}")
    # tcl.eval(f"set argv {{{' '.join(argi)}}}")
    completer = NestedCompleter.from_nested_dict(completions)


    try:
        Path("/home/claudio/.opensees-history").touch()
        session = PromptSession(history=FileHistory("/home/claudio/.opensees-history"))
    except:
        session = PromptSession()

    print(intro)
    while True:
        inputs = nested_prompt(session, [('class:prompt',PROMPT)], vi_mode=use_vi,
        # inputs = session.prompt([('class:prompt',PROMPT)], vi_mode=use_vi, 
                    style=style,
                    lexer=PygmentsLexer(TclLexer),
                    completer=completer,
                    complete_while_typing=False
        )
        try:
            value = tcl.eval(inputs)
            if value:
                print(value)
        except Exception as e:
            #raise
            print(e)

