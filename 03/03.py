file = open('input.txt', 'r') 
lines = file.readlines()
map = []

#part 1
for line in lines:
    row = []
    for char in line:
        if (char == ".") or (char == "#"):
            row.append(char)
    map.append(row)

current_col = 0
trees = 0
for row in range(0, len(map)):

    if (map[row][current_col] == "#"):
        trees = trees + 1
    current_col = current_col + 3 # flytta tre sidledes

    #om vi är utanför, fixa det
    if (current_col > len(map[row]) - 1):
        current_col = current_col % len(map[row])


print("Antal träd")
print(trees)

#part 2

def count_trees(map, down, right):
    current_col = 0
    trees = 0
    for row in range(0, len(map), down):

        if (map[row][current_col] == "#"):
            trees = trees + 1
        current_col = current_col + right # flytta sidledes

        #om vi är utanför, fixa det
        if (current_col > len(map[row]) - 1):
            current_col = current_col % len(map[row])
    return trees
    
t1 = count_trees(map, 1, 1)
t2 = count_trees(map, 1, 3)
t3 = count_trees(map, 1, 5)
t4 = count_trees(map, 1, 7)
t5 = count_trees(map, 2, 1)
sum = t1 * t2 * t3 * t4 * t5
print(f"Summan bli då {sum}")