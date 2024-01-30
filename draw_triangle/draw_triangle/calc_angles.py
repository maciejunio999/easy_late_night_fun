import math

def calculate_angles(sides):
    e = []
    for i in range(0,3):
        c = sides[i]
        s = sides[:]
        s.pop(i)
        a, b = s
        angle = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
        e.append(angle)
    
    x1, x2, x3 = math.degrees(e[0]), math.degrees(e[1]), math.degrees(e[2])
    results = [x3, x1, x2]
    r_0 = results[0]
    results[0] = 180 - results[0]
    results[1] = (results[2] * 2) + r_0 + results[1]

    return results