def max_jolt_2(batteries):
    total = 0
    for battery in batteries:
        i = 0
        j = 1
        left = 0
        right = 0
        while j < len(battery): 
            left = max(left, int(battery[i]))
            right = max(right, int(battery[j]))
            if left < right and j + 1 < len(battery):
                i = j
                j += 1
                right = int(battery[j])
            else: 
                j += 1
        total += 10 * left + right
    return total

def max_jolt_12(batteries):
    total = 0
    for battery in batteries:
        stack = []
        to_remove = len(battery) - 12
        for char in battery: 
            while stack and to_remove > 0 and stack[-1] < char:
                stack.pop()
                to_remove -= 1
            stack.append(char)
        max_jolt = ''.join(stack[:12])
        total += int(max_jolt)
    return total

test = """987654321111111
811111111111119
234234234234278
818181911112111"""

input_file = open('03-lobby.txt')
batteries = []
for line in input_file.read().split('\n'):
    batteries.append(line.strip())
        
print(max_jolt_2(batteries))
print(max_jolt_12(batteries))