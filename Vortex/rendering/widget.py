# external imports
import pyglet
from pyglet.gl import *


class VortexBoundingBox:
    """
    VortexBoundinBox

    A class to make bounding boxes easier.
    """

    def __init__(self, x, y, width, height):
        """
        __init__

        Initialize the bounding box.

        x: The x coordinate of the top left corner.
        y: The y coordinate of the top left corner.
        width: The width of the bounding box.
        height: The height of the bounding box.

        return: self
        """
        self.x = x  # x coordinate
        self.y = y  # y coordinate
        self.width = width  # width
        self.height = height  # height

    def contains(self, x, y):
        """
        contains

        Check if the bounding box contains the given coordinates.

        x: The x coordinate.
        y: The y coordinate.

        return: bool
        """
        return self.x <= x and x <= self.x + self.width and self.y <= y and y <= self.y + self.height  # check if the coordinates are inside the bounding box

    def intersects(self, other):
        """
        intersects

        Check if the bounding box intersects with another bounding box.

        other: The other bounding box.

        return: bool
        """
        return self.x <= other.x + other.width and other.x <= self.x + self.width and self.y <= other.y + other.height and other.y <= self.y + self.height  # check if the bounding boxes intersect

    def __str__(self):
        """
        __str__

        Return the string representation of the bounding box.

        return: str
        """
        return "BoundingBox(x={}, y={}, width={}, height={})".format(self.x, self.y, self.width, self.height)  # return the string representation of the bounding box


vortex_default_bounding_box = VortexBoundingBox(
    10, 10, 40, 40)  # the default bounding box


class VortexWidgetBase:
    """
    VortexWidgetBase

    This class is the base class of all widgets.
    """

    def __init__(self, parent):
        """
        __init__

        Initialize the widget.

        parent: The parent widget.

        return: self
        """
        self.bounding_box = vortex_default_bounding_box  # the bounding box
        self.parent = parent  # the parent widget

    def __str__(self):
        """
        __str__

        Return the string representation of the widget.

        return: str
        """
        return "Widget(bounding_box={})".format(self.bounding_box)  # return the string representation of the widget


class VortexTextWidget(VortexWidgetBase):
    """
    VortexTextWidget

    This class is a text widget.
    """

    def __init__(self, parent, text, bounding_box):
        """
        __init__

        Initialize the text widget.

        parent: The parent widget.
        text: The text of the widget.
        bounding_box: The bounding box of the widget.

        return: self
        """
        super().__init__(parent)  # initialize the base class
        self.bounding_box = bounding_box  # the bounding box
        self.text = text  # the text
        self.props = {  # the properties, stored in a dictionary
            "font_size": 12,
            "font_name": "Arial",
            "color": (255, 255, 255, 255),
            "background": (0, 0, 0, 255),
        }

        self.label = pyglet.text.Label(text,  # create the label
                                       # use this.props
                                       font_size=self.props["font_size"],
                                       font_name=self.props["font_name"],
                                       color=self.props["color"],
                                       x=self.bounding_box.x, y=self.bounding_box.y,
                                       batch=self.parent.batch,
                                       )

    def __str__(self):
        # return the string representation of the text widget
        return "TextWidget(text={}, bounding_box={})".format(self.text, self.bounding_box)


class VortexInfo(VortexWidgetBase):
    """
    VortexInfo

    This class is a text widget which shows whats going on in the browser.
    """

    def __init__(self, parent):
        """
        __init__

        Initialize the text widget.

        parent: The parent widget.

        return: self
        """
        super().__init__(parent)  # initialize the base class
        self.text = "Info appears here"  # the default text
        self.props = {  # the properties, stored in a dictionary
            "font_size": 12,
            "font_name": "Arial",
            "color": (255, 255, 255, 255),
        }

        self.label = pyglet.text.Label(self.text,  # create the label
                                       # use this.props
                                       font_size=self.props["font_size"],
                                       font_name=self.props["font_name"],
                                       color=self.props["color"],
                                       x=self.bounding_box.x, y=self.bounding_box.y,
                                       batch=self.parent.batch,
                                       )

        self.fade = 255  # the fade value

    def update(self):
        """
        update

        Update the widget.

        return: None
        """
        if self.fade != 0:  # if the fade value is not 0
            self.fade -= 1  # decrease the fade value
            # set the color of the label
            self.label.color = (255, 255, 255, self.fade)

    def set_text(self, text):
        """
        set_text

        Set the text of the widget.

        text: The text.

        return: None
        """
        self.text = text  # set the text
        self.label.text = text  # set the text of the label
        self.fade = 255  # set the fade value

    def __str__(self):
        """
        __str__

        Return the string representation of the widget.

        return: str
        """
        return "TextWidget(text={}, bounding_box={})".format(self.text, self.bounding_box)  # return the string representation of the text widget
