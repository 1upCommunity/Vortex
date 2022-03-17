import pyglet
from pyglet.window import *

class VortexWindow(Window):
    def __init__(self):
        super().__init__(resizable=True)
        self.rendering_list = []
        self.batch = pyglet.graphics.Batch()
        
        # window props
        self.width = 1800
        self.height = 600
        self.resizable = True
        self.tab_bar_height = 20

        self.set_caption("Vortex")

    def on_draw(self):
        self.clear()
        self.batch.draw()

        for widget in self.rendering_list:
            widget.render()
