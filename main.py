import myinputobject
import mygeometry
import myconstraints
import matplotlib.pyplot as plt
import numpy as np
from sympy import *


def main():
    inputObject = myinputobject.InputObject()

    fig, ax = plt.subplots(1)

    furnitureobjects = mygeometry.FurnituresObjects()

    for rectangle in inputObject.rectangleTupleList:
        rectangleObj = mygeometry.Rectangle(inputObject, rectangle[0], rectangle[1])
        furnitureobjects.rectangleObjectArray.append(rectangleObj)
        furnitureobjects.rectangleArray.append(rectangleObj.patplot())

    for circle in inputObject.circleList:
        circleObj = mygeometry.Circle(inputObject, circle)
        furnitureobjects.circleObjectArray.append(circleObj)
        furnitureobjects.circleArray.append(circleObj.patplot())

    for i in range(len(furnitureobjects.circleObjectArray)):
        for j in range(i + 1, len(furnitureobjects.circleObjectArray)):
            print("1")
            print(furnitureobjects.circleObjectArray)
            furnitureobjects = myconstraints.overlay_constraint_circle_circle(furnitureobjects,
                                                                              furnitureobjects.circleObjectArray[i],
                                                                              furnitureobjects.circleObjectArray[j])
            print(furnitureobjects.circleObjectArray)

    for i in range(len(furnitureobjects.rectangleArray)):
        for j in range(i + 1, len(furnitureobjects.rectangleArray)):
            print("2")
            furnitureobjects = myconstraints.overlay_constraint_rectangle_rectangle(furnitureobjects,
                                                                                    furnitureobjects.rectangleArray[i],
                                                                                    furnitureobjects.rectangleArray[j])

    for rectangle in furnitureobjects.rectangleObjectArray:
        for circle in furnitureobjects.circleObjectArray:
            furnitureobjects = myconstraints.overlay_constraint_rectangle_circle(furnitureobjects, rectangle, circle)

    # triangle = pat.Polygon(xy=[[0, 0.3], [0.3, 0.3], [0.15, 0.4]], closed=True)

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

    plt.title('Your Room could look like this:')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


if __name__ == "__main__":
    main()
