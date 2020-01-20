from math import sqrt
import myinputobject
import mygeometry
import matplotlib.patches as pat
import shapely.geometry


def overlay_constraint_rectangle_circle(rectangle, circle, rectangleObj, circleObj) -> bool:
    b = False

    def createLine(t1, t2):
        delta_x = t2[0] - t1[0]
        delta_y = t2[1] - t1[1]
        m = delta_y / delta_x
        c = t1[1] - m * t1[0]
        return m, c

    r = circle.get_radius()

    # TODO for every edge and line
    # P1
    m, c = createLine((rectangle.get_x(), rectangle.get_y()),
                      (rectangle.get_x() + rectangle.get_width(), rectangle.get_y()))
    xm = circle.get_center()[0]
    ym = circle.get_center()[1]

    # solution for simplity:
    Discriminant = (-2 * xm + 2 * m * c - 2 * m * ym) ** 2 - 4 * (1 + m ** 2) * (
            xm ** 2 + c ** 2 + ym ** 2 - r ** 2 - 2 * c * ym)

    while Discriminant > 0:
        # delete the object I compared with
        circleObj.__del__()
        # create new object
        inputObject = myinputobject.InputObject()
        circleObj = mygeometry.Circle(inputObject, inputObject.circle_r)
        circle = pat.Circle(xy=(circleObj.x_circle, circleObj.y_circle), radius=circleObj.circle_r)
        # compare again
        Discriminant = overlay_constraint_rectangle_circle(rectangle, circle, rectangleObj, circleObj)

    if Discriminant <= 0:
        b = True
        print("finally True")
    return b


def overlay_constraint_circle_circle(c1, c2, circleObj, circleObj2) -> bool:
    b = False
    m1 = c1.get_center()
    m2 = c2.get_center()

    distanceM1M2 = sqrt((m2[0] - m1[0]) ** 2 + (m2[1] - m1[1]) ** 2)

    if abs(c1.get_radius() - c2.get_radius()) < distanceM1M2 < abs(c1.get_radius() + c2.get_radius()):
        # delete the object I compared with
        circleObj.__del__()
        # create new object
        inputObject = myinputobject.InputObject()
        circleObj = mygeometry.Circle(inputObject, inputObject.circle_r)
        c1 = pat.Circle(xy=(circleObj.x_circle, circleObj.y_circle), radius=circleObj.circle_r)
        overlay_constraint_circle_circle(c1, c2, circleObj, circleObj2)

    if (abs(c1.get_radius() - c2.get_radius()) > distanceM1M2) or (
            distanceM1M2 > abs(c1.get_radius() + c2.get_radius())):
        b = True

    return b


def overlay_constraint_rectangle_rectangle(rectangle, rectangle2) -> bool:
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
        inputObject = myinputobject.InputObject()
        b = True
        rectangleObj = mygeometry.Rectangle(inputObject, inputObject.rectangle1_width, inputObject.rectangle1_height)

        rectangle = pat.Rectangle(xy=(rectangleObj.x_rectangle, rectangleObj.y_rectangle),
                                  width=rectangleObj.width_rectangle, height=rectangleObj.height_rectangle,
                                  angle=inputObject.angle_rectangle)
        overlay_constraint_rectangle_rectangle(rectangle, rectangle2)

    return b
