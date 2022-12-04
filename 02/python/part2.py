f = open("input_example.txt", "r")
score = 0
score_lookup = {"Y":2,"X":1,"Z":3,"A Y":6,"B Y":3,"C Y":0,"A X":3,"B X":0,"C X":6,"A Z":0,"B Z":6,"C Z":3}
pick_lookup = {"A X":"Z", "A Y":"X", "A Z":"Y", \
    "B X":"X", "B Y":"Y", "B Z":"Z", \
    "C X":"Y", "C Y":"Z", "C Z":"X"}
"""
    A=rock, B=paper, C=scissors
    X=rock, Y=paper, Z=scissors

    X=lose, Y=draw, Z=win
"""
for line in f.readlines():
    line = line.replace("\n","")
    our_pick = pick_lookup[line]
    score += score_lookup[our_pick]
    score += score_lookup[f"{line.split(' ')[0]} {our_pick}"]

print(score)
