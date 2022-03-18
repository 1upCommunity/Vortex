# internal imports
from rendering import VortexInfo

# external imports
import pyglet
from pyglet.window import Window


class VortexWindow(Window):
    """
    VortexWindow

    This class is the main window of the application.
    """

    def __init__(self):
        """
        __init__

        initialize the window

        return: self
        """
        super().__init__(resizable=True)  # initialize the base class
        self.batch = pyglet.graphics.Batch()  # create a batch
        self.frame = 0  # frame counter

        self.resizable = True  # allow resizing
        self.tab_bar_height = 20  # tab bar height
        self.set_caption("Vortex")  # set window title
        self.set_icon(pyglet.image.load( # logo image
            "assets/VortexLogoTransparent.png"))

        self.info_label = VortexInfo(self)  # create the info label

        pyglet.clock.schedule_interval(self.on_update, 1/60)  # schedule update
        pyglet.clock.schedule_once(self.refresh_size, 0)  # schedule draw

    def refresh_size(self, *args):
        """
        refresh_size

        A solution to the wierd white line that appears 
        in the starting and goes away after the first resize.

        *args: Receives the pyglet dt argument.

        return: None
        """
        self.set_size(self.width, self.height)  # set the size of the window

    def on_draw(self):
        """
        on_draw

        Draw the window.

        return: None
        """
        self.clear()  # clear the window
        self.batch.draw()  # draw the batch

    def on_update(self, dt):
        """
        on_update

        Update the window.

        dt: The time since the last update. 

        return: None
        """
        self.frame += 1  # increment the frame counter
        self.info_label.update()  # update the info label
