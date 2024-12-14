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

    def quad_score(t):
        i = -1
        j = -1
        quad_count = [0]*4
        ans = 1
        for i in range(len(positions)):
            pos = [(positions[i][0]+t*velocities[i][0]) % grid_dim[0],(positions[i][1]+t*velocities[i][1]) % grid_dim[1]]
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
        
        for c in quad_count:
            ans *= c
        
        return ans
    
    t = 0
    scores = [quad_score(t)]
    min_score = scores[0]
    MAX_TIME = 10000
    while t <= MAX_TIME:
        t += 1
        new_score = quad_score(t)
        if new_score < min_score:
            min_score = new_score
            min_t = t
        scores.append(new_score)
    return scores[100], min_t

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