import numpy as np
import time
start_time = time.time() 

def input_to_pv(data):
    positions = []
    velocities = []
    lines = data.split('\n')
    for line in lines:
        parts = line.split(' ')
        pos = parts[0][2:].split(',')
        positions.append([int(pos[0]),int(pos[1])])
        vel = parts[1][2:].split(',')
        velocities.append([int(vel[0]),int(vel[1])])

    return positions, velocities

def solve(positions, velocities, grid_dim):
    quad_count = [0]*4
    quads = [[],[],[],[]]

    def add_to_quad(pos):
        i = -1
        j = -1
        if 0 <= pos[0] < grid_dim[0]//2:
            i = 0
        elif grid_dim[0]//2 < pos[0]:
            i = 1
        if 0 <= pos[1] < grid_dim[1]//2:
            j = 0
        elif grid_dim[1]//2 < pos[1]: 
            j = 1
        
        if i in [0,1] and j in [0,1]:
            quad_count[i+2*j] += 1
            quads[i+2*j].append(pos)

    for i in range(len(positions)):
        new_pos = [(positions[i][0]+100*velocities[i][0]) % grid_dim[0],(positions[i][1]+100*velocities[i][1]) % grid_dim[1]]
        add_to_quad(new_pos)

    ans = 1
    for c in quad_count:
        ans *= c

    t = 0
    positions_t = [pos[:] for pos in positions]
    def check_tree(points):
        max_in_a_row = 1
        for p in points:
            in_a_row = 1
            while [p[0]+in_a_row,p[1]] in points:
                in_a_row += 1
            max_in_a_row = max(max_in_a_row,in_a_row)
        
        if max_in_a_row > 10:
            return True
        return False

    while not check_tree(positions_t):
        t += 1
        positions_t = []
        for i in range(len(positions)):
            positions_t.append([(positions[i][0]+t*velocities[i][0]) % grid_dim[0],(positions[i][1]+t*velocities[i][1]) % grid_dim[1]])
    return ans, t  

test_data = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

with open('14_restroom_redoubt.txt', 'r') as file:
    data = file.read() 

positions, velocities = input_to_pv(data)
print(solve(positions, velocities,[101,103]))

print("--- %s seconds ---" % (time.time() - start_time))