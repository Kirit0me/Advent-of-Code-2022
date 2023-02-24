import time

start = time.time()
useless_elves = 0
with open("day4.txt", "r") as meow:
    for soji in meow:
        soji_elves = soji.strip().split(",")
        soji_time_1 = [int(x) for x in soji_elves[0].split("-")]
        soji_time_2 = [int(x) for x in soji_elves[1].split("-")]
        # part 1 : if ((soji_time_1[0] <= soji_time_2[0]) and (soji_time_1[1] >= soji_time_2[1])) or ((soji_time_2[0] <= soji_time_1[0]) and (soji_time_2[1] >= soji_time_1[1])):
        if((soji_time_2[1] >= soji_time_1[0]) and (soji_time_1[1]>= soji_time_2[0])):  
            useless_elves += 1

print("Number of useless elves : ", useless_elves)
stop = time.time()
print(stop - start)