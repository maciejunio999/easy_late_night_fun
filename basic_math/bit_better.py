# gets area fo triangle based on coorginates of three points
# but with randomized points

import random

list = {f'p{i}': (i, random.randint(0,10)) for i in range(1, 4)}

def area(list_of_points):
    return 0.5 * abs(
        ((list_of_points['p2'][0] - list_of_points['p1'][0]) * 
         (list_of_points['p3'][1] - list_of_points['p1'][1])) - 
        ((list_of_points['p2'][1] - list_of_points['p1'][1]) * 
         (list_of_points['p3'][0] - list_of_points['p1'][0])))

print(list)
print(area(list))
