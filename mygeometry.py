import random
import numpy as np
import matplotlib.patches as pat


class FurnituresObjects(object):

    def __init__(self):
        self.circleObjectArray = []
        self.rectangleArray = []
        self.circleArray = []
        self.rectangleObjectArray = []

    def __del__(self):
        pass


class Circle(object):

    def __init__(self, input, circle_r):
        self.circle_r = circle_r
        # Create Randomness
        xmax = np.max(input.room_x_coord)
        ymax = np.max(input.room_y_coord)

        self.x_circle = round(random.uniform(0, xmax), 2)
        self.y_circle = round(random.uniform(0, ymax), 2)

        # TODO adjust for every shape/ room
        if (self.y_circle <= 150):
            self.xmax = 300

        if self.x_circle + input.circle_r > xmax:
            self.x_circle = xmax - input.circle_r
        if self.y_circle + input.circle_r > ymax:
            self.y_circle = ymax - input.circle_r

        if self.x_circle - input.circle_r < 0:
            self.x_circle = 0 + input.circle_r
        if self.y_circle - input.circle_r < 0:
            self.y_circle = 0 + input.circle_r

        pass

    def patplot(self):
        circle = pat.Circle(xy=(self.x_circle, self.y_circle), radius=self.circle_r)

        return circle

    def __del__(self):

        pass


class Rectangle(object):
    def __init__(self, input, width_rectangle, height_rectangle):
        self.width_rectangle = width_rectangle
        self.height_rectangle = height_rectangle
        # TODO constraint to room edges
        self.xmax = np.max(input.room_x_coord)
        self.ymax = np.max(input.room_y_coord)

        self.x_rectangle = round(random.uniform(0, self.xmax), 2)
        self.y_rectangle = round(random.uniform(0, self.ymax), 2)

        # TODO adjust for every shape/ room
        if (self.y_rectangle <= 150):
            self.xmax = 300

        if (self.x_rectangle + width_rectangle) > self.xmax:
            self.x_rectangle = self.xmax - self.width_rectangle
        if self.y_rectangle + height_rectangle > self.xmax:
            self.y_rectangle = self.ymax - self.height_rectangle
        if (self.x_rectangle + width_rectangle) < 0:
            self.x_rectangle = 0 + self.width_rectangle
        if self.y_rectangle + height_rectangle < 0:
            self.y_rectangle = 0 + self.height_rectangle

        pass

    def patplot(self):
        rectangle = pat.Rectangle(xy=(self.x_rectangle, self.y_rectangle),
                                  width=self.width_rectangle, height=self.height_rectangle,
                                  angle=0)

        return rectangle

    def __del__(self):
        pass