# gives middles of three sides of triangle based on three points

point1 = (0, 0)
point2 = (4, 0)
point3 = (0, 4)

def middle(p1, p2):
    return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)

print(middle(point1, point2))
print(middle(point2, point3))
print(middle(point1, point3))