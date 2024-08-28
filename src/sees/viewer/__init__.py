# Claudio Perez
# Summer 2024
import textwrap
from pathlib import Path

class Viewer:
    def __init__(self, viewer=None, src=None):
        self._glbsrc = "./model.glb" if src is None else src
        self._viewer = viewer if viewer is not None else "mv"

    def get_html(self):
        if self._viewer == "three-160":
            with open(Path(__file__).parents[0]/"gltf.html", "r") as f:
                return f.read()

        elif self._viewer == "three-130":
            with open(Path(__file__).parents[0]/"index.html", "r") as f:
                return f.read()

        elif self._viewer == "mv":
            return textwrap.dedent(f"""
          <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
            "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
          <html xmlns="http://www.w3.org/1999/xhtml" lang="en">
          <head>
            <meta charset="utf-8">
            <script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.5.0/model-viewer.min.js">
            </script>
          </head>
          <body>
            <model-viewer alt="rendering"
                          src="{self._glbsrc}"
                          ar
                          style="width: 100%; height: 1000px;"
                          shadow-intensity="1" camera-controls touch-action="pan-y">
            </model-viewer>
          </body>
          </html>
        """)

