def calibrate1(amended):
    ans = 0
    for char in amended:
        if char.isnumeric():
            ans = 10*int(char)
            break
    for char in amended[::-1]:
        if char.isnumeric():
            ans += int(char)
            break
    return ans

def calibrate2(amended):
    ans = 0
    nums = {'one':1,
            'two':2,
            'three':3,
            'four':4,
            'five':5,
            'six':6,
            'seven':7,
            'eight':8,
            'nine':9}
    # find index where words first/last appear
    # find index where numerals first/last appear
    # compare indices and return ans
    first_word_idx = len(amended)
    last_word_idx = -1
    for key in nums:
        index = amended.find(key)
        if index != -1:
            if index < first_word_idx:
                first_word_idx = index
                first_word = nums[key]
            if index > last_word_idx:
                last_word_idx = index
                last_word = nums[key]
    
    first_num_idx = len(amended)
    last_num_idx = -1
    for i, c in enumerate(amended):
        if c.isnumeric():
            first_num_idx = i
            first_num = int(c)
            break
        
    for j, c in enumerate(amended[::-1]):
        if c.isnumeric():
            last_num_idx = len(amended)-1-j
            last_num = int(c)
            break

    #print(first_word_idx, first_num_idx, last_word_idx, last_num_idx)
    if first_word_idx < first_num_idx:
        ans = first_word
    else:
        ans = first_num
    ans *= 10
    if last_word_idx > last_num_idx:
        ans += last_word
    else:
        ans += last_num

    return ans
        

input_file = open('trebuchet.txt')
inputs = input_file.readlines()
total1 = 0
total2 = 0
for line in inputs:
    total1 += calibrate1(line)
    total2 += calibrate2(line)

print(total1)
print(total2)
input_file.close()
