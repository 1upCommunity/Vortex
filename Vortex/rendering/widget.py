import pyglet
from pyglet.gl import *

class VortexBoundingBox:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def contains(self, x, y):
        return self.x <= x and x <= self.x + self.width and self.y <= y and y <= self.y + self.height

    def intersects(self, other):
        return self.x <= other.x + other.width and other.x <= self.x + self.width and self.y <= other.y + other.height and other.y <= self.y + self.height

    def __str__(self):
        return "BoundingBox(x={}, y={}, width={}, height={})".format(self.x, self.y, self.width, self.height)

vortex_default_bounding_box = VortexBoundingBox(10, 10, 40, 40)

class VortexWidgetBase:
    def __init__(self, parent):
        self.bounding_box = vortex_default_bounding_box
        self.parent = parent
        self.parent.render_list.append(self)

        self.to_render = []

    def render(self):
        for detail in self.to_render:
            if detail[0] == "text":
                pyglet.text.Label(detail[1], x=detail[2], y=detail[3], batch=self.parent.batch)

    def __str__(self):
        return "Widget(bounding_box={})".format(self.bounding_box)

class VortexTextWidget(VortexWidgetBase):
    def __init__(self, parent, text, bounding_box):
        super().__init__(parent)
        self.bounding_box = bounding_box
        self.to_render.append(["text", text, bounding_box])

    def __str__(self):
        return "TextWidget(text={}, bounding_box={})".format(self.text, self.bounding_box)
