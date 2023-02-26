#I hardcoded the stacks list so u can try doing that too

import time
start = time.time()
sui_stack = [[],
             ["G", "T", "R", "W"], 
             ["G", "C", "H", "P", "M", "S", "V", "W"], 
             ["C", "L", "T", "S", "G", "M"], 
             ["J", "H", "D", "M", "W", "R", "F"], 
             ["P", "Q", "L", "H", "S", "W", "F", "J"], 
             ["P", "J", "D", "N", "F", "M", "S"],
             ["Z", "B", "D", "F", "G", "C", "S", "J"],
             ["R", "T", "B"],
             ["H", "N", "W", "L", "C"]]

start = time.time()
with open("day5.txt", "r") as port_navy:
    cargo=port_navy.readlines()

for boxes in cargo:
    instructions = boxes.split(" ")
    number_of_boxes = int(instructions[1])
    from_cargo = int(instructions[3])
    to_cargo = int(instructions[5])
    #part 1
    '''for i in range(number_of_boxes):
        box = sui_stack[from_cargo].pop()
        sui_stack[to_cargo].append(box)'''

    boxsei = sui_stack[from_cargo][-number_of_boxes:]
    #print(list(boxsei))
    #print(sui_stack)
    sui_stack[to_cargo] = sui_stack[to_cargo] + boxsei

    #alt method for 2
    #for i in range(number_of_boxes):
     #   sui_stack[from_cargo].pop()

    sui_stack[from_cargo] = sui_stack[from_cargo][:len(sui_stack[from_cargo])-number_of_boxes]
    #print(sui_stack[from_cargo], sui_stack[to_cargo], boxsei)'''
    
print(sui_stack)
stop = time.time()
print(stop - start)