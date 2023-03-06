#code taken from https://github.com/silentw0lf/advent_of_code_2022/blob/main/07/solve.py

from collections import defaultdict
import time
start = time.time()

with open("day7.txt", 'r') as f:
    commands = f.readlines()

sizes = defaultdict(int)
stack = []

for c in commands:
    if c.startswith("$ ls") or c.startswith("dir"):
        continue
    if c.startswith("$ cd"):
        dest = c.split()[2]
        if dest == "..":
            stack.pop()
        else:
            path = f"{stack[-1]}_{dest}" if stack else dest
            stack.append(path)
    else:
        size, file = c.split()
        for path in stack:
            sizes[path] += int(size)

needed_size = 30000000 - (70000000 - sizes["/"])
for size in sorted(sizes.values()):
    if size > needed_size:
        break

stop = time.time()

print(sum(n for n in sizes.values() if n <= 100000)) # task 1
print(size) # task 2

print(stop-start)

