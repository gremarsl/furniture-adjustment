from math import sqrt
import myinputobject
import mygeometry
import shapely.geometry


def overlay_constraint_rectangle_circle(furnitureObject, rectangleObj, circleObj) -> mygeometry.FurnituresObjects:
    def createLine(t1, t2):
        delta_x = t2[0] - t1[0]
        delta_y = t2[1] - t1[1]
        m = delta_y / delta_x
        c = t1[1] - m * t1[0]
        return m, c

    r = circleObj.circle_r

    # TODO for every edge and line
    # P1
    m, c = createLine((rectangleObj.x_rectangle, rectangleObj.y_rectangle),
                      (rectangleObj.x_rectangle + rectangleObj.width_rectangle, rectangleObj.y_rectangle))
    xm = circleObj.x_circle
    ym = circleObj.y_circle

    # solution for simplity:
    Discriminant = (-2 * xm + 2 * m * c - 2 * m * ym) ** 2 - 4 * (1 + m ** 2) * (
            xm ** 2 + c ** 2 + ym ** 2 - r ** 2 - 2 * c * ym)

    while Discriminant > 0:
        circleObj.__del__()
        print("del-fun Circle was called:")
        # create new object
        inputObject = myinputobject.InputObject()
        newcircleObj = mygeometry.Circle(inputObject, circleObj.circle_r)

        #check if rectangle ok:

        #if ok add to array:
        furnitureObject.circleObjectArray.append(newcircleObj)
        furnitureObject.circleArray.append(newcircleObj.patplot())
        # compare again

        # TODO exit recursion when correct once!!
        overlay_constraint_rectangle_circle(furnitureObject, rectangleObj, newcircleObj)

    if Discriminant <= 0:
        pass
    return furnitureObject


def overlay_constraint_circle_circle(furnitureObject, circleObj, circleObj2) -> mygeometry.FurnituresObjects:
    m1 = (circleObj.x_circle, circleObj.y_circle)
    m2 = (circleObj2.x_circle, circleObj2.y_circle)

    distanceM1M2 = sqrt((m2[0] - m1[0]) ** 2 + (m2[1] - m1[1]) ** 2)

    if abs(circleObj.circle_r - circleObj2.circle_r) < distanceM1M2 < abs(circleObj.circle_r + circleObj2.circle_r):
        # delete the object I compared with
        circleObj.__del__()
        print("del-fun Circle ")
        # create new object
        inputObject = myinputobject.InputObject()

        newcircleObj = mygeometry.Circle(inputObject, inputObject.circle_r)
        furnitureObject.circleObjectArray.append(newcircleObj)
        furnitureObject.circleArray.append(newcircleObj.patplot())

        furnitureObject = overlay_constraint_circle_circle(furnitureObject, newcircleObj, circleObj2)

    if (abs(circleObj.circle_r - circleObj2.circle_r) > distanceM1M2) or (
            distanceM1M2 > abs(circleObj.circle_r + circleObj2.circle_r)):
        pass
    return furnitureObject


def overlay_constraint_rectangle_rectangle(furnitureObject, rectangle, rectangle2) -> mygeometry.FurnituresObjects:
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
        inputObject = myinputobject.InputObject()
        newrectangleObj = mygeometry.Rectangle(inputObject, rectangle.get_width(), rectangle.get_width())
        furnitureObject.rectangleObjectArray.append(newrectangleObj)
        furnitureObject.rectangleArray.append(newrectangleObj.patplot())

        furnitureObject = overlay_constraint_rectangle_rectangle(furnitureObject, newrectangleObj.patplot(), rectangle2)

    return furnitureObject
