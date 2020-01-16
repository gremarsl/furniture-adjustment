import shapely.geometry
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import random
from sympy import *
import numpy as np

class InputObject(object):

    #Room
    e1 = (0, 0)
    e2 = (0, 500)
    e3 = (350, 500)
    e4 = (350, 150)
    e5 = (300, 150)
    e6 = (300, 0)
    e7 = (0, 0)

    elist = []
    elist.extend((e1, e2,e3, e4,e5,e6,e7))

    i = 0
    room_x_coord = []
    room_y_coord = []
    for element in elist:
        room_x_coord.append(element[0])
        room_y_coord.append(element[1])
    arr = []
    arr.extend((room_x_coord, room_y_coord))

    # Circle
    circle_r = 30

    #Rectangle1
    rectangle1_width = 100
    rectangle1_height = 100

    # Rectangle2
    rectangle2_width = 10
    rectangle2_height = 50

    #all Rectangles
    angle_rectangle = 0
    def __init__(self):
        pass

class Circle(object):

    def __init__(self):
        pass

class Rectangle(object):

    def __init__(self):
        pass


def overlay_constraint_rectangle_circle(rectangle, circle):
    def createLine(t1, t2):
        delta_x = t2[0] - t1[0]
        delta_y = t2[1] - t1[1]
        m = delta_y / delta_x
        c = t1[1] - m * t1[0]
        return m, c

    # TODO for every edge and Strecke
    m, c = createLine((rectangle.get_x(), rectangle.get_y()),
                      (rectangle.get_x() + rectangle.get_width(), rectangle.get_y()))
    r = circle.get_radius()
    xm = circle.get_center()[0]
    ym = circle.get_center()[1]

    # solution for simplity:
    Discriminant = (-2 * xm + 2 * m * c - 2 * m * ym) ** 2 - 4 * (1 + m ** 2) * (
                xm ** 2 + c ** 2 + ym ** 2 - r ** 2 - 2 * c * ym)
    print(Discriminant)
    return Discriminant


def overlay_constraint_circle_circle(c1, c2) -> float:
    m1 = c1.get_center()
    m2 = c2.get_center()

    distance = sqrt((m2[0] - m1[0]) ** 2 + (m2[1] - m1[1]) ** 2)
    print(distance)
    return distance


def overlay_constraint_rectangle_rectangle(rectangle, rectangle2):
    b = False
    rectangle_blueprint = shapely.geometry.Polygon([(rectangle.get_x(), rectangle.get_y()),
                                                    (rectangle.get_x() + rectangle.get_width(), rectangle.get_y()),
                                                    (rectangle.get_x() + rectangle.get_width(),
                                                     rectangle.get_y() + rectangle.get_height()),
                                                    (rectangle.get_x(), rectangle.get_y() + rectangle.get_height())
                                                    ])

    rectangle2_blueprint = shapely.geometry.Polygon([(rectangle2.get_x(), rectangle2.get_y()),
                                                     (rectangle2.get_x() + rectangle2.get_width(), rectangle2.get_y()),
                                                     (rectangle2.get_x() + rectangle2.get_width(),
                                                      rectangle2.get_y() + rectangle2.get_height()),
                                                     (rectangle2.get_x(), rectangle2.get_y() + rectangle2.get_height())
                                                     ])

    if rectangle_blueprint.intersects(rectangle2_blueprint):
        print(rectangle_blueprint.intersects(rectangle2_blueprint))
        b = True

    return b


def createRectangle(input,width_rectangle, height_rectangle):
    #TODO constraint to room edges
    xmax = np.max(input.arr)
    ymax = np.max(input.arr)
    x_rectangle = round(random.uniform(0, xmax), 2)
    y_rectangle = round(random.uniform(0, ymax), 2)
    if (x_rectangle + width_rectangle) > xmax:
        x_rectangle = xmax- width_rectangle
    if y_rectangle + height_rectangle > xmax:
        y_rectangle = ymax - height_rectangle
    if (x_rectangle + width_rectangle) < 0:
        x_rectangle = 0 + width_rectangle
    if y_rectangle + height_rectangle < 0:
        y_rectangle = 0 + height_rectangle

    print("examiniation")
    print(width_rectangle)
    print(height_rectangle)
    rectangle = pat.Rectangle(xy=(x_rectangle, y_rectangle), width=width_rectangle, height=height_rectangle,
                              angle=input.angle_rectangle)
    return rectangle


def createCircle(input):
    # Create Randomness
    xmax = np.max(input.arr)
    ymax=np.max(input.arr)
    x_circle = round(random.uniform(0, xmax), 2)
    y_circle = round(random.uniform(0, ymax), 2)

    if x_circle + input.circle_r > xmax:
        x_circle = xmax - input.circle_r
    if y_circle + input.circle_r > ymax:
        y_circle = ymax - input.circle_r

    if x_circle - input.circle_r < 0:
        x_circle = 0 + input.circle_r
    if y_circle - input.circle_r < 0:
        y_circle = 0 + input.circle_r

    circle = pat.Circle(xy=(x_circle, y_circle), radius=input.circle_r)
    return circle


def createRoom(input):

    elist = []
    elist.extend((input.e1, input.e2, input.e3, input.e4,input.e5,input.e6,input.e7))
    print(elist)

    i = 0
    xplist = []
    yplist = []
    for element in elist:
        xplist.append(element[0])
        yplist.append(element[1])

    return xplist,yplist


def main():
    inputObject=InputObject()

    fig, ax = plt.subplots(1)

    circle = createCircle(inputObject)
    circle2 = createCircle(inputObject)
    rectangle = createRectangle(inputObject,width_rectangle=inputObject.rectangle1_width, height_rectangle=inputObject.rectangle1_height)
    rectangle2 = createRectangle(inputObject,width_rectangle=inputObject.rectangle2_width, height_rectangle=inputObject.rectangle2_height)

    b = overlay_constraint_rectangle_rectangle(rectangle, rectangle2)

    while b == True:
        rectangle2 = createRectangle(width_rectangle=100, height_rectangle=100)
        b = overlay_constraint_rectangle_rectangle(rectangle, rectangle2)

    Discriminant = overlay_constraint_rectangle_circle(rectangle, circle)

    while Discriminant > 0:
        circle = createCircle(30)
        Discriminant = overlay_constraint_rectangle_circle(rectangle, circle)

    distance = overlay_constraint_circle_circle(circle, circle2)

    while (abs(circle.get_radius() - circle2.get_radius())) < distance < (
    abs(circle.get_radius() + circle2.get_radius())):
        circle = createCircle(30)
        distance = overlay_constraint_circle_circle(circle, circle2)
        print(distance)

    #TODO how to manage, that when generated new geometry -> every condition is checked
    triangle = pat.Polygon(xy=[[0, 0.3], [0.3, 0.3], [0.15, 0.4]], closed=True)


    ax.add_patch(circle)
    ax.add_patch(circle2)

    ax.add_patch(rectangle)
    ax.add_patch(rectangle2)
    ax.add_patch(triangle)

    plt.xlim(right=np.max(inputObject.arr)+1)  # xmax is your value
    plt.xlim(left=np.min(inputObject.arr)-1)  # xmin is your value
    plt.ylim(top=np.max(inputObject.arr)+1)  # ymax is your value
    plt.ylim(bottom=np.min(inputObject.arr)-1)  # ymin is your value
    plt.plot(inputObject.room_x_coord,inputObject.room_y_coord)
    plt.plot()

    plt.title('Scatter plot pythonspot.com')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    print("Done")


if __name__ == "__main__":
    main()
