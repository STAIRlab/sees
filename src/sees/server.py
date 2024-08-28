#===----------------------------------------------------------------------===#
#
#         STAIRLab -- STructural Artificial Intelligence Laboratory
#
#===----------------------------------------------------------------------===#
#
# Claudio Perez
# Summer 2024
import sys
import bottle
from .viewer import Viewer

class Server:
    def __init__(self, glb=None, html=None, artist=None, viewer=None):
        # Create App
        self._app = bottle.Bottle()

        if glb is not None:
            self._source = "glb"
            html = Viewer(src="./model.glb",
                          viewer=viewer).get_html()

            # Create routes
            self._app.route("/model.glb")(lambda : glb  )
            self._app.route("/")(lambda          : html )

        elif artist is not None:
            self._source = "artist"

        else:
            self._source = "html"
            # Create routes
            self._app.route("/")(lambda : html )

    def run(self, port=None):
        if port is None:
            port = 8082

        try:
            bottle.run(self._app, host="localhost", port=port)
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":

    options = {
        "viewer": None
    }
    filename = sys.argv[1]

    with open(filename, "rb") as f:
        glb = f.read()

    Server(glb=glb, **options).run()


