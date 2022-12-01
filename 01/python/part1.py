f = open("input.txt", "r")
max_calories = 0
tmp = 0
for line in f.readlines():
    if line == "\n":
        if tmp > max_calories:
            max_calories = tmp
        tmp = 0
    else:
        tmp += int(line)
print(max_calories) 
f.close()