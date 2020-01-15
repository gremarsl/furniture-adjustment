import shapely.geometry
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import random
from sympy import *
import numpy as np


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


def createRectangle(width_rectangle, height_rectangle):
    x_rectangle = round(random.uniform(0, 1), 2)
    y_rectangle = round(random.uniform(0, 1), 2)
    if (x_rectangle + width_rectangle) > 1:
        x_rectangle = 1 - width_rectangle
    if y_rectangle + height_rectangle > 1:
        y_rectangle = 1 - height_rectangle
    if (x_rectangle + width_rectangle) < 0:
        x_rectangle = 0 + width_rectangle
    if y_rectangle + height_rectangle < 0:
        y_rectangle = 0 + height_rectangle

    angle_rectangle = 0
    rectangle = pat.Rectangle(xy=(x_rectangle, y_rectangle), width=width_rectangle, height=height_rectangle,
                              angle=angle_rectangle)
    return rectangle


def createCircle(r_circle=0.1):
    # Create Randomness
    x_circle = round(random.uniform(0, 1), 2)
    y_circle = round(random.uniform(0, 1), 2)

    if x_circle + r_circle > 1:
        x_circle = 1 - r_circle
    if y_circle + r_circle > 1:
        y_circle = 1 - r_circle

    if x_circle - r_circle < 0:
        x_circle = 0 + r_circle
    if y_circle - r_circle < 0:
        y_circle = 0 + r_circle

    circle = pat.Circle(xy=(x_circle, y_circle), radius=r_circle)
    return circle


def main():
    fig, ax = plt.subplots(1)

    circle = createCircle(0.1)
    circle2 = createCircle(0.1)
    rectangle = createRectangle(width_rectangle=0.2, height_rectangle=0.2)
    rectangle2 = createRectangle(width_rectangle=0.2, height_rectangle=0.2)

    b = overlay_constraint_rectangle_rectangle(rectangle, rectangle2)

    while b == True:
        rectangle2 = createRectangle(width_rectangle=0.2, height_rectangle=0.2)
        b = overlay_constraint_rectangle_rectangle(rectangle, rectangle2)

    Discriminant = overlay_constraint_rectangle_circle(rectangle, circle)

    while Discriminant > 0:
        circle = createCircle(0.1)
        Discriminant = overlay_constraint_rectangle_circle(rectangle, circle)

    distance = overlay_constraint_circle_circle(circle, circle2)

    while (abs(circle.get_radius() - circle2.get_radius())) < distance < (
    abs(circle.get_radius() + circle2.get_radius())):
        circle = createCircle(0.1)
        distance = overlay_constraint_circle_circle(circle, circle2)
        print(distance)

    triangle = pat.Polygon(xy=[[0, 0.3], [0.3, 0.3], [0.15, 0.4]], closed=True)

    ax.add_patch(circle)
    ax.add_patch(circle2)

    ax.add_patch(rectangle)
    ax.add_patch(rectangle2)
    ax.add_patch(triangle)

    plt.xlim(right=1)  # xmax is your value
    plt.xlim(left=0)  # xmin is your value
    plt.ylim(top=1)  # ymax is your value
    plt.ylim(bottom=0)  # ymin is your value
    plt.plot()

    plt.title('Scatter plot pythonspot.com')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    print("Done")


if __name__ == "__main__":
    main()
