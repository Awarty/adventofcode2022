import numpy as np
f = open("input.txt", "r")
max_calories = [0, 0, 0]
tmp = 0
for line in f.readlines():
    if line == "\n":
        min_index = max_calories.index(min(max_calories))
        if (max_calories[min_index] < tmp):
            max_calories[min_index] = tmp
        tmp = 0
    else:
        tmp += int(line)

min_index = max_calories.index(min(max_calories))
if (max_calories[min_index] < tmp):
    max_calories[min_index] = tmp

print(max_calories)
print(np.sum(max_calories))
f.close()

