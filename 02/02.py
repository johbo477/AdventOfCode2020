import re

file = open('input.txt', 'r') 
lines = file.readlines()

valid = 0
#part 1
for line in lines:
    m = re.match("(\d+)-(\d+) (.): (.*)", line)
    if m:
        min = int(m.group(1))
        max = int(m.group(2))
        char = m.group(3)
        password = m.group(4)
        found = 0
        for c in password:
            if (c == char):
                found = found + 1
        if (found >= min and found <= max):
            valid = valid + 1
print("Valid passwords: ")
print(valid)

# part 2
valid = 0
for line in lines:
    m = re.match("(\d+)-(\d+) (.): (.*)", line)
    if m:
        pos1 = int(m.group(1))
        pos2 = int(m.group(2))
        char = m.group(3)
        password = m.group(4)
        none = (not password[pos1 - 1] == char) and (not password[pos2 - 1] == char)
        both = password[pos1 - 1] == char and password[pos2 - 1] == char
        if (not none and not both):
            valid = valid + 1
print("Valid passwords: ")
print(valid)
