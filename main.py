import myinputobject
import mygeometry
import myconstraints
import matplotlib.pyplot as plt
import numpy as np
from sympy import *

def main():
    inputObject = myinputobject.InputObject()

    fig, ax = plt.subplots(1)

    furnitureobjects=mygeometry.FurnituresObjects()

    #Make the variable a function attribute

    circleObj = mygeometry.Circle(inputObject, inputObject.circle_r)
    furnitureobjects.circleObjectArray.append(circleObj)
    furnitureobjects.circleArray.append(circleObj.patplot())
    circleObj2 = mygeometry.Circle(inputObject, inputObject.circle_r)
    furnitureobjects.circleObjectArray.append(circleObj2)
    furnitureobjects.circleArray.append(circleObj2.patplot())

    rectangleObj = mygeometry.Rectangle(inputObject, inputObject.rectangle1_width, inputObject.rectangle1_height)
    furnitureobjects.rectangleObjectArray.append(rectangleObj)
    furnitureobjects.rectangleArray.append(rectangleObj.patplot())

    rectangleObj2 = mygeometry.Rectangle(inputObject, inputObject.rectangle2_width, inputObject.rectangle2_height)
    furnitureobjects.rectangleObjectArray.append(rectangleObj2)
    furnitureobjects.rectangleArray.append(rectangleObj2.patplot())


    #TODO what happens in the array? if object is deleted
    for i in range(len(furnitureobjects.circleObjectArray)):
        for j in range(i + 1, len(furnitureobjects.circleObjectArray)):
            print(furnitureobjects.circleObjectArray)
            myconstraints.overlay_constraint_circle_circle(furnitureobjects.circleObjectArray[i], furnitureobjects.circleObjectArray[j])
            print(furnitureobjects.circleObjectArray)

    for i in range(len(furnitureobjects.rectangleArray)):
        for j in range(i + 1, len(furnitureobjects.rectangleArray)):
            myconstraints.overlay_constraint_rectangle_rectangle(furnitureobjects.rectangleArray[i], furnitureobjects.rectangleArray[j])

    for rectangle in furnitureobjects.rectangleObjectArray:
        for circle in furnitureobjects.circleObjectArray:
            myconstraints.overlay_constraint_rectangle_circle(rectangle,circle)

    #triangle = pat.Polygon(xy=[[0, 0.3], [0.3, 0.3], [0.15, 0.4]], closed=True)

    for element in furnitureobjects.circleArray:
        ax.add_patch(element)

    for element in furnitureobjects.rectangleArray:
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

