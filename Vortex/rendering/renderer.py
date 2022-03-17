import pyglet, rendering, pygame
from pyglet.gl import *
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

        # Create tab display
        self.tab_display = rendering.VortexTabDisplay(self)

        # refresh rate
        pyglet.clock.schedule_interval(self.on_update, 1/60)

    def on_draw(self):
        self.clear()
        self.batch.draw()

        self.tab_display.draw()
        for widget in self.rendering_list:
            widget.render()

    def on_update(self, dt):
        self.tab_display.update()

    def on_close(self):
        pygame.quit()
        exit()

    def on_resize(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, width, 0, height, -1, 1)
        glMatrixMode(GL_MODELVIEW)
