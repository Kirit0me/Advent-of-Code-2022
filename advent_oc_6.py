import time
start = time.time()

with open('day6.txt', 'r') as nyan:
    letters = nyan.read()

for n in range(len(letters)):
    if len(set(letters[n:n+14])) == 14:
        print(n+14)
        break

stop = time.time()
print(stop - start)
#This one was boring.