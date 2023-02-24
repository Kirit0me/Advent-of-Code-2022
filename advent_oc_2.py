import time

'''start = time.time()
with open("day2.txt", "r") as meow:
    nyan = meow.readlines()

def nyanify(elf, kiri):
    points_ftw = 0
    
    match elf:
        case "A":
            match kiri:
                case "X":
                    points_ftw += 4
                case "Y":
                    points_ftw += 8
                case "Z":
                    points_ftw += 3
        case "B":
            match kiri:
                case "X":
                    points_ftw += 1
                case "Y":
                    points_ftw += 5
                case "Z":
                    points_ftw += 9
        case "C":
            match kiri:
                case "X":
                    points_ftw += 7
                case "Y":
                    points_ftw += 2
                case "Z":
                    points_ftw += 6

    return points_ftw

suisei = []
for cats in nyan:
    suisei.append(nyanify(cats[0], cats[2]))

print(sum(suisei))
stop = time.time()
print(stop - start)'''


start = time.time()
with open("day2.txt", "r") as meow:
    nyan = meow.readlines()

def nyanify(elf, kiri):
    points_ftw = 0
    
    match elf:
        case "A":
            match kiri:
                case "X":
                    points_ftw += 3
                case "Y":
                    points_ftw += 4
                case "Z":
                    points_ftw += 8
        case "B":
            match kiri:
                case "X":
                    points_ftw += 1
                case "Y":
                    points_ftw += 5 
                case "Z":
                    points_ftw += 9
        case "C":
            match kiri:
                case "X":
                    points_ftw += 2
                case "Y":
                    points_ftw += 6
                case "Z":
                    points_ftw += 7

    return points_ftw

suisei = []
for cats in nyan:
    suisei.append(nyanify(cats[0], cats[2]))

print(sum(suisei))
stop = time.time()
print(stop - start)