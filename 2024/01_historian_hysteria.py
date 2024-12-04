def find_diff(left, right):
    total = 0
    for i in range(len(left)):
        total += abs(left[i]-right[i])
    return total

def find_similarity(left, right):
    total = 0
    i = 0
    j = 0
    left_count = 1
    right_count = 0
    last_left = left[0]
    while i <= len(left):
        if i < len(left) and last_left == left[i]:
            left_count += 1
            i += 1
        elif last_left == right[j]:
            right_count += 1
            j += 1
        elif last_left > right[j]:
            j += 1
        else:
            total += last_left*left_count*right_count
            last_left = left[i] if i < len(left) else None
            left_count = 1
            right_count = 0
            i += 1
        
    return total

input_file = open('01_historian_hysteria.txt')
left = []
right = []
for line in input_file:
    num1, num2 = map(int, line.split())
    left.append(num1)
    right.append(num2)

left.sort()
right.sort()
print(find_diff(left, right))
print(find_similarity(left, right))