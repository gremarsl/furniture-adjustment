import myinputobject as myinputobject
import mygeometry as mygeometry
import myconstraints
import matplotlib.patches as pat
import matplotlib.pyplot as plt
import numpy as np
from sympy import *


def main():
    inputObject = myinputobject.InputObject()

    fig, ax = plt.subplots(1)

    circleObjectArray=[]
    rectangleArray=[]
    circleArray=[]
    rectangleObjectArray=[]

    circleObj = mygeometry.Circle(inputObject, inputObject.circle_r)
    circleObjectArray.append(circleObj)
    circleArray.append(circleObj.patplot())

    circleObj2 = mygeometry.Circle(inputObject, inputObject.circle_r)
    circleObjectArray.append(circleObj2)
    circleArray.append(circleObj2.patplot())

    rectangleObj = mygeometry.Rectangle(inputObject, inputObject.rectangle1_width, inputObject.rectangle1_height)
    rectangleObjectArray.append(rectangleObj)
    rectangle = pat.Rectangle(xy=(rectangleObj.x_rectangle, rectangleObj.y_rectangle),
                              width=rectangleObj.width_rectangle, height=rectangleObj.height_rectangle,
                              angle=inputObject.angle_rectangle)
    rectangleArray.append(rectangle)

    rectangleObj2 = mygeometry.Rectangle(inputObject, inputObject.rectangle2_width, inputObject.rectangle2_height)
    rectangleObjectArray.append(rectangleObj2)
    rectangle2 = pat.Rectangle(xy=(rectangleObj2.x_rectangle, rectangleObj2.y_rectangle),
                               width=rectangleObj2.width_rectangle, height=rectangleObj2.height_rectangle,
                               angle=inputObject.angle_rectangle)
    rectangleArray.append(rectangle2)

    '''
    #TODO what happens in the array? if object is deleted
    for i in range(len(circleArray)):
        for j in range(i + 1, len(circleArray)):
            myconstraints.overlay_constraint_circle_circle(circleArray[i], circleArray[j])

    for i in range(len(rectangleArray)):
        for j in range(i + 1, len(rectangleArray)):
            myconstraints.overlay_constraint_rectangle_rectangle(rectangleArray[i], rectangleArray[j])

    for rectangle in rectangleObjectArray:
        for circle in circleArray:
            myconstraints.overlay_constraint_rectangle_circle(rectangle,circle)

    myconstraints.overlay_constraint_rectangle_circle(rectangleObj, circleObj)
'''
    #triangle = pat.Polygon(xy=[[0, 0.3], [0.3, 0.3], [0.15, 0.4]], closed=True)

    for element in circleArray:
        ax.add_patch(element)

    for element in rectangleArray:
        ax.add_patch(element)

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
