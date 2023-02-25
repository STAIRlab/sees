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

class OpenSeesREPL:
    """
    Create an OpenSees read-eval-print loop (REPL).
    """
    prompt = "opensees \N{WHITE PARALLELOGRAM} "

    def __init__(self, interp=None):
        import opensees
        import time, sys

        if interp is None:
            self.interp = opensees.tcl.TclRuntime(verbose=False)
        else:
            self.interp = interp

        self.interp.eval(file_util_commands)

        try:
            Path("/home/claudio/.opensees-history").touch()
            self.session = PromptSession(history=FileHistory("/home/claudio/.opensees-history"))
        except:
            self.session = PromptSession()

    def repl(self):
        use_vi = True
        prompt = self.prompt
        completions.update({
            k: None for k in self.interp.eval("info commands").split() if k not in completions
        })
        # tcl.eval(f"set argc {len(sys.argv) - 2}")
        # tcl.eval(f"set argv {{{' '.join(argi)}}}")
        completer = NestedCompleter.from_nested_dict(completions)

        interp = self.interp

        interp.eval("puts $opensees::banner")

        while True:
            inputs = nested_prompt(self.session, [('class:prompt',prompt)], vi_mode=use_vi,
                        style=style,
                        lexer=PygmentsLexer(TclLexer),
                        completer=completer,
                        complete_while_typing=False
            )
            try:
                value = interp.eval(inputs)
                if value is not None and value != "":
                    print(value)
            except Exception as e:
                # print(e)
                pass

