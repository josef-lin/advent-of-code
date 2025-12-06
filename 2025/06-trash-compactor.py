def eval_problems1(problems, operators):
    results = problems[0][:]
    for i in range(1, len(problems)):
        problem = problems[i]
        for j, num in enumerate(problem):
            operator = operators[j]
            if operator == '+':
                results[j] += num
            else:
                results[j] *= num
    return sum(results)

def eval_problems2(problems, operators):
    results = []
    for i in range(len(problems)):
        ans = 0
        if '*' == operators[i]:
            ans = 1
        for num in problems[i]:
            if '+' == operators[i]:
                ans += num
            else:
                ans *= num
        results.append(ans)
    return sum(results)


test = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

input_file = open('06-trash-compactor.txt')

problems1 = []
operators1 = []

# for line in test.strip().split('\n'):
#     line = line.strip()
#     if line[0] in '+*':
#         for char in line:
#             if char in '+*':
#                 operators1.append(char)
#     else:
#         nums = []
#         val = 0
#         for char in line:
#             if char == ' ':
#                 if val != 0:
#                     nums.append(val)
#                     val = 0
#             else:
#                 val = 10 * val + int(char)
#         if val != 0:
#             nums.append(val)
#         problems1.append(nums)

for line in input_file:
    line = line.strip()
    if line[0] in '+*':
        for char in line:
            if char in '+*':
                operators1.append(char)
    else:
        nums = []
        val = 0
        for char in line:
            if char == ' ':
                if val != 0:
                    nums.append(val)
                    val = 0
            else:
                val = 10 * val + int(char)
        if val != 0:
            nums.append(val)
        problems1.append(nums)

input_matrix = []
problem_id = 0
problems2 = [[]]
operators2 = []

# lines = test.split('\n')
# input_matrix = [list(line.ljust(len(line)))[::-1] for line in lines]

input_file = open('06-trash-compactor.txt')
for line in input_file:
    input_matrix.append(list(line.strip('\n'))[::-1])

for j in range(len(input_matrix[0])):
    num = 0
    for i in range(len(input_matrix)-1):
        if input_matrix[i][j] != " ":
            num = 10 * num + int(input_matrix[i][j])
    if num != 0:
        problems2[problem_id].append(num)

    if input_matrix[-1][j] in "+*":
        operators2.append(input_matrix[-1][j])
        problem_id += 1
        problems2.append([])
problems2 = problems2[:-1]


print(eval_problems1(problems1, operators1))
print(eval_problems2(problems2, operators2))