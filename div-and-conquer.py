import sys
from math import sqrt, inf

def make_points(input):    # Time complexity O(n)
    px = []
    py = [] 
    for i in range(N):                                  
        x, y = list(map(int, input[i].split(' ')))
        px.append(x)
        py.append(y)
    return zip(px, py)

def distance(p1, p2):
    return sqrt( (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 )

def brute(Px, size):      # Time complexity O(1)
    d = distance(Px[0], Px[1])
    if size == 2: 
        return d
    if size == 3: 
        return min(d, distance(Px[0], Px[2]), distance(Px[1], Px[2]))

def closest_pair(Px, Py, size):
    if size < 4:
        return brute(Px, size)

    mid = size // 2
    Lx = Px[:mid]
    Rx = Px[mid:]
    Ly = []
    Ry = []
    set_of_lx = set(Lx)

    for point in Py:                    # Time complexity O(n)
        if point in set_of_lx:
            Ly.append(point)
        else:
           Ry.append(point)
    
    left_distance = closest_pair(Lx, Ly, mid)
    right_distance = closest_pair(Rx, Ry, size - mid)  
    delta = min(left_distance, right_distance)
    middle_x = Rx[0][0]

    def within_delta(point):
        return abs( point[0] - middle_x) < delta
    S = [point for point in Px if within_delta(point)]  # Time complexity O(<n)
    S = set(S)
    if not S:
        return delta
    Sy = [point for point in Py if point in S]          # Time complexity O(s) < O(n)
    if not Sy:
        return delta

    listLength = len(Sy)                                
    for i in range(listLength - 1):                     # Time complexity < O(n)
        for j in range(i+1, min(i + 15, listLength)):
            dst = distance(Sy[i], Sy[j])
            if dst < delta:
                delta = dst
    return delta 

input_lines = sys.stdin.read().strip().split('\n')
N = int(input_lines[0])

# Python sorted function uses Timsort (hybrid sorting algorithm, 
# derived from merge sort and insertion sort) with 'Worst-case performance' O(nlog n)
P_x = sorted(make_points(input_lines[1:]), key=lambda x: x[0]) 
P_y = sorted(P_x,key=lambda y: y[1]) 
shortest_dist = closest_pair(P_x, P_y, N)
print("{:.6f}".format(shortest_dist))
