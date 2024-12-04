
def string_to_mat(s):
    matrix = [list(row) for row in s.strip().split('\n')]
    return matrix

def count_xmas(mat):
    count = 0
    word = 'XMAS'
    rows = len(mat)
    cols = len(mat[0])
    directions = [(0,1),
                  (-1,0),
                  (1,0),
                  (0,-1),
                  (1,1),
                  (1,-1),
                  (-1,1),
                  (-1,-1)]
    

    def search_from(i, j, dx, dy):
        for k in range(len(word)):
            x, y = i + dx * k, j + dy * k
            if not (0 <= x < rows and 0 <= y < cols) or mat[x][y] != word[k]:
                return False
        return True

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 'X':
                for dx, dy in directions:
                    if search_from(i, j, dx, dy):
                        count += 1

    return count

def count_Xmas(mat):
    count = 0
    word = 'MAS'
    rows = len(mat)
    cols = len(mat[0])
    directions = [(1,1,-1,1),
                  (1,1,1,-1),
                  (-1,-1,-1,1),
                  (-1,-1,1,-1)]

    def search_from(i, j, dx1, dy1, dx2, dy2):
        for k in range(-1,2):
            x, y = i + dx1 * k, j + dy1 * k
            if not (0 <= x < rows and 0 <= y < cols) or mat[x][y] != word[k+1]:
                return False
        for k in range(-1,2):
            x, y = i + dx2 * k, j + dy2 * k
            if not (0 <= x < rows and 0 <= y < cols) or mat[x][y] != word[k+1]:
                return False
        return True
    
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 'A':
                for dx1, dy1, dx2, dy2 in directions:
                    if search_from(i, j, dx1, dy1, dx2, dy2):
                        count += 1

    return count

test_string = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
with open('04_ceres_search.txt', 'r') as file:
    input_file = file.read() 

mat = string_to_mat(input_file)
print(count_xmas(mat))
print(count_Xmas(mat))