class InputObject(object):
    # Room
    e1 = (0, 0)
    e2 = (0, 500)
    e3 = (350, 500)
    e4 = (350, 150)
    e5 = (300, 150)
    e6 = (300, 0)
    e7 = (0, 0)

    elist = []
    elist.extend((e1, e2, e3, e4, e5, e6, e7))

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

    # Rectangle1
    rectangle1_width = 100
    rectangle1_height = 100

    # Rectangle2
    rectangle2_width = 10
    rectangle2_height = 50

    # all Rectangles
    angle_rectangle = 0

    def __init__(self):
        pass

