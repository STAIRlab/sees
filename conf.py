# Configuration file for the Sphinx documentation builder.
#
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
from pathlib import Path
project = 'OpenSeesRT'
copyright = '2023, Claudio M. Perez'
author = 'Claudio M. Perez'
description = "Lightning-fast integration for single-degree-of-freedom systems."
abstract = r"""
This package solves scalar differential equations of the form

   $$m \ddot{u} + c \dot{u} + k u = f(t)$$

Integration is carried out using a Generalized - :math:`\alpha`
integrator that is implemented under the hood in highly optimized
multi-threaded C code.
"""

version = '0.0.0'
release = '0.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'nbsphinx',
    'sphinx_design',
    'myst_parser',
#   'sphinx_c_autodoc',
#   'sphinx_c_autodoc.napoleon'
]

import pathlib
if pathlib.Path('/usr/lib/libclang.so').is_file():
    import clang.cindex
    clang.cindex.Config.set_library_file('/usr/lib/libclang.so')
c_autodoc_roots = ['../src/']

myst_enable_extensions = ["dollarmath", "amsmath"]

templates_path   = ['_templates']
exclude_patterns = [
        ".*/",
        "library/modules/*",
        "library/modules/"
]

from sphinxcontrib.pandoc_markdown import MarkdownParser
source_suffix = '.rst'
source_suffix = [source_suffix, '.md', source_suffix]
source_parsers = {
   '.md': MarkdownParser,
}
root_doc = 'index'
language = 'en'

# -- Options for HTML output -------------------------------------------------

html_title = project
html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']
html_favicon = '_static/favicon.ico'
html_css_files = [
    "css/peer.css",
] + [
    'css/css/'+str(file.name) for file in (Path(__file__).parents[0]/"_static/css/css/").glob("*.css")
]
html_additional_pages = {'index': 'home.html', 'OpenSeesRT': 'sdof.html'}
html_context = {
    'description': description,
    'highlights': {
        "": "Because <code>OpenSeesRT</code> is implemented in standard C, linking should never be a problem.",
        ".": "Both C11 threads and Posix threading is supported"
    },
    "examples": [
        {"title": "Python Basics", "link": "examples/OpenSeesRT-0001/index", "image": "OpenSeesRT-0001.png",
         "description": ""},
        {"title": "Live App", "link": "examples/OpenSeesRT-0002/index", "image": "OpenSeesRT-0001.png",
         "description": ""},
        {"title": "Spectra from C", "link": "examples/OpenSeesRT-0003/index", "image": "OpenSeesRT-0001.png",
         "description": ""},
    ],
    **globals()
}
html_show_sourcelink = False
html_theme_options = {
    "show_nav_level": 5,
    "collapse_navigation": False,
    "github_url": f"https://github.com/BRACE2/{project}",
}

autodoc_member_order = 'bysource'
