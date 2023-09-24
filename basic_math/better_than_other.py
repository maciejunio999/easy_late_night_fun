# fusion of easy_one, bit_better and other_easy

import random

list = {f'p{i}': (i, random.randint(0,10)) for i in range(1, 4)}

def middle(p1, p2):
    return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)

def middles(list_of_points):
    length = len(list_of_points.keys())
    result = {}
    for i in range(1, length):
        for j in range(i+1, length+1):
            result[f'middle of points {i} and {j}'] = middle(list_of_points[f'p{i}'], list_of_points[f'p{j}'])
    return result

print(list)
print(middles(list))