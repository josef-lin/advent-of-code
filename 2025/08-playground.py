import heapq

def playground(positions, connections):
    n = len(positions)
    heap = build_heap(positions)
    k = 0
    parent = list(range(n))
    rank = [0] * n
    size = [1] * n

    def find(a): 
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False 
        if rank[ra] < rank[rb]:
            parent[ra] = rb
            size[rb] += size[ra]
        elif rank[ra] > rank[rb]:
            parent[rb] = ra
            size[ra] += size[rb]
        else: 
            parent[rb] = ra
            rank[ra] += 1
            size[ra] += size[rb]
        return True

    selected = []
    while k < connections:
        dist, i, j = heapq.heappop(heap)
        if union(i, j):
            selected.append([dist, i, j])
        k += 1

    sorted_a = sorted(size, reverse=True)
    ans_a = sorted_a[0] * sorted_a[1] * sorted_a[2]

    while max(size) < n:
        dist, i, j = heapq.heappop(heap)
        if union(i, j):
            selected.append([dist, i, j])
    
    final_d, final_i, final_j = selected[-1]
    ans_b = positions[final_i][0] * positions[final_j][0]
    return ans_a, ans_b

def build_heap(positions):
    heap = []
    n = len(positions)
    for i in range(n):
        for j in range(i):
            heapq.heappush(heap, (distance(positions[i], positions[j]), i, j))
    return heap

def distance(pos1, pos2):
    return (sum([(pos1[i]-pos2[i])**2 for i in range(len(pos1))]))**(1/2)

test = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

input_file = open('08-playground.txt')

positions = []
# for line in test.split('\n'):
#     positions.append([int(coord) for coord in line.split(',')])

for line in input_file:
    positions.append([int(coord) for coord in line.split(',')])

connections = 1000

print(playground(positions, connections))