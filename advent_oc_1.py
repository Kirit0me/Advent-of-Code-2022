#part 2 cuz I edited part 1 code and cba

import time

start = time.time()
with open("day1.txt", "r") as inventory:
    items=inventory.readlines()

cal_max = []
cal_sum = 0
for item in items:
    if item == "\n":
        cal_max.append(cal_sum)
        cal_sum = 0
    else:
        cal_sum += int(item)

print(sum(sorted(cal_max)[-3:]))

stop = time.time()
print(stop - start)


