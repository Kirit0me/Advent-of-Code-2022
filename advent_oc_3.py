import time
import string

start = time.time()

with open("advent3.txt", "r") as meow:
    nyan = meow.readlines()

suisei = 0
#part 1
for word in nyan:
    mid = int(len(word)/2)

    a, b = word[mid:], word[:mid]
    for common_sense in a:
        if common_sense in b:
            if common_sense in string.ascii_lowercase:
                suisei += ord(common_sense) - ord("a") + 1
            else:
                suisei += ord(common_sense) - ord("A") + 27
            break
print(suisei)
#part2
sike = 0
for sike in range(0, int(len(nyan)/3)):
    a, b, c = nyan[sike*3], nyan[sike*3 + 1], nyan[sike*3 + 2]
    for common_sense in a:
        if (common_sense in b) and (common_sense in c):
            if common_sense in string.ascii_lowercase:
                suisei += ord(common_sense) - ord("a") + 1
            else:
                suisei += ord(common_sense) - ord("A") + 27
            break 


print(suisei)
stop = time.time()
print(stop - start)

