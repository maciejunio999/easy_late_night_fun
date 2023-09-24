# gets area fo triangle based on coorginates of three points

point1 = (0, 0)
point2 = (3, 0)
point3 = (0, 3)

def area(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    a = 0.5 * abs(((x2 - x1) * (y3 - y1)) - ((y2 - y1) * (x3 - x1)))
    return a

print(area(point1, point2, point3))