import random
import inputobject as inputobject
import mygeometry as mygeometry
import constraints as constraints
import matplotlib.patches as pat
import matplotlib.pyplot as plt
import numpy as np
from sympy import *

def createRectangle(input, width_rectangle, height_rectangle):
    # TODO constraint to room edges
    xmax = np.max(input.arr)
    ymax = np.max(input.arr)
    x_rectangle = round(random.uniform(0, xmax), 2)
    y_rectangle = round(random.uniform(0, ymax), 2)
    if (x_rectangle + width_rectangle) > xmax:
        x_rectangle = xmax - width_rectangle
    if y_rectangle + height_rectangle > xmax:
        y_rectangle = ymax - height_rectangle
    if (x_rectangle + width_rectangle) < 0:
        x_rectangle = 0 + width_rectangle
    if y_rectangle + height_rectangle < 0:
        y_rectangle = 0 + height_rectangle

    rectangle = pat.Rectangle(xy=(x_rectangle, y_rectangle), width=width_rectangle, height=height_rectangle,
                              angle=input.angle_rectangle)
    return rectangle


def createCircle(input,radius):
    # Create Randomness
    xmax = np.max(input.arr)
    ymax = np.max(input.arr)
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
    # need to exe in main: ax.add_patch(circle)
    return circle

def main():
    inputObject = inputobject.InputObject()

    fig, ax = plt.subplots(1)

    circleObj = mygeometry.Circle(inputObject, inputObject.circle_r)
    circle = pat.Circle(xy=(circleObj.x_circle, circleObj.y_circle), radius=circleObj.circle_r)

    circleObj2 = mygeometry.Circle(inputObject, inputObject.circle_r)
    circle2 = pat.Circle(xy=(circleObj2.x_circle, circleObj2.y_circle), radius=circleObj2.circle_r)

    circleObject = mygeometry.Circle(inputObject, inputObject.circle_r)
    circle3 = pat.Circle(xy=(circleObject.x_circle, circleObject.y_circle), radius=circleObject.circle_r)

    rectangleObj = mygeometry.Rectangle(inputObject, inputObject.rectangle1_width, inputObject.rectangle1_height)

    rectangle = pat.Rectangle(xy=(rectangleObj.x_rectangle, rectangleObj.y_rectangle),
                              width=rectangleObj.width_rectangle, height=rectangleObj.height_rectangle,
                              angle=inputObject.angle_rectangle)

    rectangleObj2 = mygeometry.Rectangle(inputObject, inputObject.rectangle2_width, inputObject.rectangle2_height)

    rectangle2 = pat.Rectangle(xy=(rectangleObj2.x_rectangle, rectangleObj2.y_rectangle),
                               width=rectangleObj2.width_rectangle, height=rectangleObj2.height_rectangle,
                               angle=inputObject.angle_rectangle)

    # TODO change to Object as parameters
    b = constraints.overlay_constraint_rectangle_rectangle(rectangle, rectangle2)

    while b:
        rectangle2 = createRectangle(inputObject,width_rectangle=100, height_rectangle=100)
        b = constraints.overlay_constraint_rectangle_rectangle(rectangle, rectangle2)

    constraints.overlay_constraint_rectangle_circle(rectangle, circle, rectangleObj, circleObj)

    distance = constraints.overlay_constraint_circle_circle(circle, circle2, circleObj, circleObj2)

    while (abs(circle.get_radius() - circle2.get_radius())) < distance < (
            abs(circle.get_radius() + circle2.get_radius())):
        circle = createCircle(inputObject,30)
        distance =constraints.overlay_constraint_circle_circle(circle, circle2,circleObj,circleObj2)
        print(distance)

    # TODO manage very overlay-condition with every geometry

    triangle = pat.Polygon(xy=[[0, 0.3], [0.3, 0.3], [0.15, 0.4]], closed=True)

    ax.add_patch(circle)
    ax.add_patch(circle2)
    ax.add_patch(circle3)

    ax.add_patch(rectangle)
    ax.add_patch(rectangle2)
    ax.add_patch(triangle)

    plt.xlim(right=np.max(inputObject.arr) + 1)  # xmax is your value
    plt.xlim(left=np.min(inputObject.arr) - 1)  # xmin is your value
    plt.ylim(top=np.max(inputObject.arr) + 1)  # ymax is your value
    plt.ylim(bottom=np.min(inputObject.arr) - 1)  # ymin is your value
    plt.plot(inputObject.room_x_coord, inputObject.room_y_coord)
    plt.plot()

    plt.title('Scatter plot pythonspot.com')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


if __name__ == "__main__":
    main()
