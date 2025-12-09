from shapely.geometry import Polygon

def largest_rectangle(positions):
    largest_area = 0
    n = len(positions)
    for i in range(n):
        for j in range(i):
            l = abs(positions[i][0] - positions[j][0]) + 1
            w = abs(positions[i][1] - positions[j][1]) + 1
            area = l*w
            if area > largest_area:
                largest_area = area
    return largest_area

def largest_colored_rectangle(positions):
    polygon = Polygon(positions)
    n = len(positions)
    max_area = 0
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = positions[i]
            x2, y2 = positions[j]
            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)
            rect = Polygon([(min_x,min_y),(max_x,min_y),(max_x,max_y),(min_x, max_y)])
            if polygon.covers(rect):
                max_area = max(max_area, (max_x - min_x + 1) * (max_y - min_y + 1))
    return max_area

test = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

input_file = open('09-movie-theater.txt')

positions = []
# for line in test.split('\n'):
    # positions.append([int(coord) for coord in line.split(',')])

for line in input_file:
    positions.append([int(coord) for coord in line.split(',')])

print(largest_rectangle(positions))
print(largest_colored_rectangle(positions))