f = open("input.txt", "r")
score = 0
score_lookup = {"Y":2,"X":1,"Z":3,"A Y":6,"B Y":3,"C Y":0,"A X":3,"B X":0,"C X":6,"A Z":0,"B Z":6,"C Z":3}
for line in f.readlines():
    line = line.replace("\n","")
    score += score_lookup[line]
    score += score_lookup[line.split(" ")[1]]
print(score)
