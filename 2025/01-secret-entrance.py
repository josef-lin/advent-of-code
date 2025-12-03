def pointing_zero(rotations):
    curr = 50
    count = 0
    for direction, value in rotations:
        if direction == 'L':
            curr = (curr - value) % 100
        else:
            curr = (curr + value) % 100
        if curr == 0:
            count += 1
    return count

def cycle_zero(rotations):
    curr = 50
    count = 0
    for direction, value in rotations:
        if direction == 'L':
            dir = -1
        else:
            dir = 1
        for _ in range(value):
            curr = (curr + dir) % 100
            if curr == 0: 
                count += 1
    return count

test = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

input_file = open('01-secret-entrance.txt')
rotations = []
for line in input_file:
    val = 0
    dir = ''
    for i, char in enumerate(line.strip()):
        if i == 0:
            dir = char
        else:
            val = 10 * val + int(char)
    rotations.append((dir, val))
        
print(pointing_zero(rotations))
print(cycle_zero(rotations))