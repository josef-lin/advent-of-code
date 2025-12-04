def count_neighbor(grid, r, c):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            count += grid[nr][nc]
    return count < 4

def count_accessible(grid):
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1 and count_neighbor(grid, r, c):
                count += 1
    return count

def remove_accessible(grid):
    new_grid = []
    count = 0
    for r in range(len(grid)):
        new_row = []
        for c in range(len(grid[0])):
            if grid[r][c] == 1 and count_neighbor(grid, r, c):
                new_row.append(0)
                count += 1
            else:
                new_row.append(grid[r][c])
        new_grid.append(new_row)
    return new_grid, count

def simulate_removal(grid):
    total_count = 0
    count = -1
    while count != 0:
        grid, count = remove_accessible(grid)
        total_count += count
    return total_count


test = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

input_file = open('04-printing-department.txt')
grid = []
for line in input_file:
    row = [] 
    for char in line.strip():
        row.append(0 if char == '.' else 1)
    grid.append(row)

# for line in test.strip().split('\n'):
#     row = [] 
#     for char in line.strip():
#         row.append(0 if char == '.' else 1)
#     grid.append(row)

print(count_accessible(grid))
print(simulate_removal(grid))