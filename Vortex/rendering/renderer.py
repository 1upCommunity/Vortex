import pyglet, core
from pyglet.gl import *
from pyglet.window import *

class VortexWindow(Window):
    def __init__(self):
        self.rendering_list = []
        self.batch = pyglet.graphics.Batch()
        super().__init__()
        
        # window props
        self.width = 1800
        self.height = 600
        self.resizable = True

        self.set_caption("Vortex")

    def on_draw(self):
        self.clear()
        self.batch.draw()

        for widget in self.rendering_list:
            widget.render()

    def on_resize(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, width, 0, height, -1, 1)
        glMatrixMode(GL_MODELVIEW)
