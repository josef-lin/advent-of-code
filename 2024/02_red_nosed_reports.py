def safe(report):
    increasing = True
    decreasing = True
    i = 1
    while i < len(report):
        if report[i] > report[i-1]:
            decreasing = False
        elif report [i] < report [i-1]:
            increasing = False
        else:
            decreasing = False
            increasing = False
        if abs(report[i]-report[i-1]) > 3:
            return False
        i += 1
    return increasing or decreasing

def modified_safe(report):
    if safe(report):
        return True
    else:
        for i in range(len(report)):
            temp = report[:i]+report[i+1:]
            if safe(temp):
                return True
    return False
    

input_file = open('02_red_nosed_reports.txt')
total = 0
modified_total = 0
for line in input_file:
    report = list(map(int, line.split()))
    if safe(report):
        total += 1
    if modified_safe(report):
        modified_total += 1

print(total)
print(modified_total)